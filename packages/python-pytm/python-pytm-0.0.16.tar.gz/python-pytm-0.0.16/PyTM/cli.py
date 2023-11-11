#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import os
import shutil
import webbrowser

import click
from rich.prompt import Confirm, Prompt
from rich.table import Table
from rich.tree import Tree
from rich.panel import Panel
from rich.layout import Layout

from PyTM import __version__, settings
from PyTM.commands.project import project, get_duration_str
from PyTM.commands.task import task
from PyTM.console import console
from PyTM.core import data_handler, invoice_handler


def init_data_store(show_messages=False):
    """
    - initializes the pytm data store.
    """
    messages = []
    messages.append("[green on white]Initializing pytm-data.\n")
    try:
        os.makedirs(settings.data_folder)
        messages.append(f"Created data folder: {settings.data_folder}")
    except Exception as _:
        messages.append(f"Data folder already exists: {settings.data_folder}")
    if not os.path.exists(settings.data_filepath):
        data_handler.init_data(settings.data_filepath)
        messages.append(f"Created data file: {settings.data_filepath}")
    else:
        messages.append(f"Data file already exists: {settings.data_filepath}")

    if not os.path.exists(settings.state_filepath):
        data_handler.init_data(
            settings.state_filepath,
            {settings.CURRENT_PROJECT: "", settings.CURRENT_TASK: ""},
        )
        messages.append(f"Created state file: {settings.state_filepath}")
    else:
        messages.append(f"State file already exists: {settings.state_filepath}")

    if show_messages:
        for message in messages:
            console.print(message)


def print_version(ctx, param, value):
    """
    shows version and exits the CLI
    :param ctx:
    :param param:
    :param value:
    :return: None
    """
    if not value:
        return
    console.print("\n[bold green]✨ PyTM ✨")
    console.print(f"version {__version__}")
    console.print("docs: https://pytm.rtfd.org")
    ctx.exit()


@click.group()
@click.option(
    "--version",
    "-v",
    "--v",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Shows version",
)
def cli():
    """
    docs: https://pytm.rtfd.org\n
    Config:\n
       default user data (optional): `pytm config user`\n
       default invoice texts & logo (optional): `pytm config invoice`
    """
    init_data_store()


@click.command(hidden=True)
def init():
    """
    - initializes & prints data files & folder.
    """
    console.print("[green on white]\nDone.")
    console.print(f"PyTM Data is stored in: {settings.data_folder}")
    console.print(f"Data file: {settings.data_filepath}")
    console.print(f"State file: {settings.state_filepath}")
    console.print(
        "\n[bold blue i on white]You also might want to run: `pytm config user` to configure default user data.[/bold blue i on white]"
    )


@click.command()
def show():
    """
    - shows list of projects and status
    """
    data = data_handler.load_data()
    state = data_handler.load_data(settings.state_filepath)
    table = Table()
    table.add_column("Project Name", style="blue bold")
    table.add_column("Created at")
    table.add_column("Status")
    for key, value in data.items():
        table.add_row(
            key,
            f'{datetime.datetime.fromisoformat(value["created_at"]).strftime("%Y, %B, %d, %H:%M:%S %p")}',
            value["status"],
        )
    message = ""
    if state[settings.CURRENT_PROJECT]:
        message += f"Active Project: [bold blue]{state[settings.CURRENT_PROJECT]}[/bold blue]\n"
    if state[settings.CURRENT_TASK]:
        message += f"Active Task: [bold green]{state[settings.CURRENT_TASK]}"
    if message:
        console.print(message)
    console.print(table)


@click.group()
def config():
    """
    - pytm sub-commands for configuration.
    """
    ...


@config.command()
def user():
    """
    - config default user.
    """
    state = data_handler.load_data(settings.state_filepath)
    current_user = {}
    if state.get("config"):
        current_user = state.get("config").get("user", {})
    else:
        state["config"] = dict()
    current_user["name"] = Prompt.ask("Name", default=current_user.get("name", ""))
    current_user["email"] = Prompt.ask("Email", default=current_user.get("email", ""))
    current_user["phone"] = Prompt.ask("Phone", default=current_user.get("phone", ""))
    current_user["address"] = Prompt.ask(
        "Address", default=current_user.get("address", "")
    )
    current_user["website"] = Prompt.ask(
        "Website", default=current_user.get("website", "")
    )
    current_user["hourly_rate"] = Prompt.ask(
        "Hourly rate in USD", default=current_user.get("hourly_rate", "")
    )
    state["config"]["user"] = current_user
    data_handler.save_data(state, settings.state_filepath)
    console.print("\n[green]Default user info updated.")


@config.command("invoice")
def config_invoice():
    """
    - configure invoice texts and logo.
    """
    state = data_handler.load_data(settings.state_filepath)
    invoice = {}
    if state.get("config"):
        invoice = state.get("config").get("invoice", {})
    else:
        state["config"] = dict()
    invoice["title"] = Prompt.ask(
        "Invoice Title", default=invoice.get("title", "Invoice")
    )
    invoice["logo"] = Prompt.ask(
        "Absolute path of a logo in .png format", default=invoice.get("logo", "")
    )
    if invoice["logo"]:
        try:
            shutil.copy2(
                invoice["logo"], os.path.join(settings.data_folder, "invoice-logo.png")
            )
            invoice["logo"] = os.path.join(settings.data_folder, "invoice-logo.png")
        except Exception as _:
            console.print("[bold red] Error occured while saving the logo.")
            console.print_exception()

    invoice["foot_note"] = Prompt.ask(
        "Foot Note?", default=invoice.get("foot_note", "Thank you for your business.")
    )
    invoice["invoice_number"] = Prompt.ask(
        "Default invoice number to start from? (integer)", default="13"
    )
    state["config"]["invoice"] = invoice
    data_handler.save_data(state, settings.state_filepath)
    console.print("\n[green]invoice texts are updated.")


@config.command(name="project")
@click.argument("project_name")
def config_project(project_name):
    """
    - config project meta data.
    """
    data = data_handler.load_data()
    if data.get(project_name):
        data[project_name]["meta"] = data.get(project_name).get("meta", {})
        data[project_name]["meta"]["title"] = Prompt.ask(
            "Project Title", default=data[project_name]["meta"].get("title", "")
        )
        data[project_name]["meta"]["billable"] = Confirm.ask(
            "Billable?", default=data[project_name]["meta"].get("billable", True)
        )
        data[project_name]["meta"]["client_name"] = Prompt.ask(
            "Client Name", default=data[project_name]["meta"].get("client_name", "")
        )
        data[project_name]["meta"]["client_email"] = Prompt.ask(
            "Client Email", default=data[project_name]["meta"].get("client_email", "")
        )
        data[project_name]["meta"]["client_phone"] = Prompt.ask(
            "Client Phone", default=data[project_name]["meta"].get("client_phone", "")
        )
        data[project_name]["meta"]["client_address"] = Prompt.ask(
            "Client Address",
            default=data[project_name]["meta"].get("client_address", ""),
        )
        data[project_name]["meta"]["client_website"] = Prompt.ask(
            "Client Website",
            default=data[project_name]["meta"].get("client_website", ""),
        )
    else:
        console.print(f"[bold red] Project {project_name} doesn't exist.")
    data_handler.save_data(data)
    console.print("\n[green]Project Meta data updated.")


@click.group()
def invoice():
    """
    - pytm sub-commands for invoice.
    """
    ...


@invoice.command()
@click.argument("project_name")
def auto(project_name):
    """
    - generates invoice for existing projects.
    """
    data = data_handler.load_data()
    if not data.get(project_name):
        console.print(f"[bold red] {project_name} doesn't exist.")
        return None
    title, logo, foot_note, invoice_number = [""] * 4
    discount = 0
    state = data_handler.load_data(settings.state_filepath)
    config = state.get("config", {})
    user = config.get("user", {})
    invoice_texts = config.get("invoice", {})
    invoice_number = Prompt.ask(
        "Invoice Number", default=invoice_texts.get("invoice_number", "13")
    )
    if state.get("config"):
        if state.get("config").get("invoice"):
            if invoice_number == state.get("config").get("invoice").get(
                "invoice_number"
            ):
                try:
                    state["config"]["invoice"][
                        "invoice_number"
                    ] = f'{int(state.get("config").get("invoice").get("invoice_number", "13")) + 1}'
                    data_handler.save_data(state, settings.state_filepath)
                except Exception as _:
                    pass

    invoice_texts["title"] = Prompt.ask(
        "Invoice Title", default=invoice_texts.get("title", "")
    )
    invoice_texts["foot_note"] = Prompt.ask(
        "Foot note", default=invoice_texts.get("foot_note", "")
    )
    invoice_texts["logo"] = Prompt.ask(
        "Logo Absolute path", default=invoice_texts.get("logo", "")
    )

    project, user = data[project_name], config.get("user", {})

    if not project["meta"]:
        project["meta"] = {}
    project["meta"]["title"] = Prompt.ask(
        "Project Name", default=f"{project['meta']['title']}"
    )
    project["created_at"] = Prompt.ask(
        "Project Date (YYYY-MM-DD)",
        default=f'{project["meta"].get("created_at", datetime.datetime.now())}',
    )
    user["name"] = Prompt.ask("Your Name", default=user.get("name", ""))
    user["email"] = Prompt.ask("Email", default=user.get("email", ""))
    user["phone"] = Prompt.ask("Phone", default=user.get("phone", ""))
    user["address"] = Prompt.ask("Address", default=user.get("address", ""))
    user["website"] = Prompt.ask("Website", default=user.get("website", ""))
    user["hourly_rate"] = Prompt.ask(
        "Hourly rate in USD", default=user.get("hourly_rate", "")
    )
    project["meta"]["client_name"] = Prompt.ask(
        "Bill To Name",
        default=f"{project['meta'].get('client_name', 'Anonymous Client')}",
    )
    project["meta"]["client_address"] = Prompt.ask(
        "Address(street, state, zip, country)",
        default=f"{project['meta'].get('client_address', 'earth')}",
    )
    project["meta"]["client_phone"] = Prompt.ask(
        "Phone", default=f"{project['meta'].get('client_phone', '')}"
    )
    project["meta"]["client_email"] = Prompt.ask(
        "Email", default=f"{project['meta'].get('client_email', '')}"
    )
    project["meta"]["client_website"] = Prompt.ask(
        "Website", default=f"{project['meta'].get('client_website', '')}"
    )
    discount = Prompt.ask("Discount?", default="")
    html = invoice_handler.generate(
        invoice_number, invoice_texts, user, project, discount
    )
    try:
        os.makedirs(os.path.join(settings.data_folder, "invoices"))
    except Exception as _:
        pass

    html_file = os.path.join(
        settings.data_folder, "invoices", f"{invoice_texts['title']}.html"
    )
    with open(html_file, "w") as f:
        f.write(html)
    console.print(f"The invoice is available in {html_file}")
    webbrowser.open(f"file:///{html_file}", autoraise=True)


@invoice.command()
def manual():
    """
    - generates invoice Solely based on prompts and config data.
    """
    title, logo, foot_note, invoice_number = [""] * 4
    discount = 0
    state = data_handler.load_data(settings.state_filepath)
    config = state.get("config", {})
    user = config.get("user", {})
    invoice_texts = config.get("invoice", {})
    invoice_number = Prompt.ask(
        "Invoice Number", default=invoice_texts.get("invoice_number", "13")
    )
    if state.get("config"):
        if state.get("config").get("invoice"):
            if invoice_number == state.get("config").get("invoice").get(
                "invoice_number"
            ):
                try:
                    state["config"]["invoice"][
                        "invoice_number"
                    ] = f'{int(state.get("config").get("invoice").get("invoice_number")) + 1}'
                    data_handler.save_data(state, settings.state_filepath)
                except Exception as _:
                    pass

    invoice_texts["title"] = Prompt.ask(
        "Invoice Title", default=invoice_texts.get("title", "")
    )
    invoice_texts["foot_note"] = Prompt.ask(
        "Foot note", default=invoice_texts.get("foot_note", "")
    )
    invoice_texts["logo"] = Prompt.ask(
        "Logo Absolute path", default=invoice_texts.get("logo", "")
    )

    project, user = {}, config.get("user", {})
    project["meta"] = {}
    project["meta"]["title"] = Prompt.ask("Project Name", default="")
    project["created_at"] = Prompt.ask(
        "Project Date (YYYY-MM-DD)", default=f"{datetime.datetime.now()}"
    )
    user["name"] = Prompt.ask("Your Name", default=user.get("name", ""))
    user["email"] = Prompt.ask("Email", default=user.get("email", ""))
    user["phone"] = Prompt.ask("Phone", default=user.get("phone", ""))
    user["address"] = Prompt.ask("Address", default=user.get("address", ""))
    user["website"] = Prompt.ask("Website", default=user.get("website", ""))
    user["hourly_rate"] = Prompt.ask(
        "Hourly rate in USD", default=user.get("hourly_rate", "")
    )
    project["meta"]["client_name"] = Prompt.ask(
        "Bill To Name", default="Anonymous Client"
    )
    project["meta"]["client_address"] = Prompt.ask(
        "Address(street, state, zip, country)", default="Earth"
    )
    project["meta"]["client_phone"] = Prompt.ask("Phone", default="")
    project["meta"]["client_email"] = Prompt.ask("Email", default="")
    project["meta"]["client_website"] = Prompt.ask("Website", default="")
    tasks = dict()
    number = 1
    while Confirm.ask("Add a task?", default=True):
        task = dict()
        task_name = Prompt.ask("Task name?", default=f"Task {number}")
        if task_name.startswith("Task"):
            number += 1
        task["description"] = Prompt.ask("Task description?", default="-")
        task["duration"] = Prompt.ask("How many hours of work? (float)", default=0.0)
        task["duration"] = float(task["duration"]) * 360
        task["status"] = settings.FINISHED
        tasks[task_name] = task
    project["tasks"] = tasks
    discount = Prompt.ask("Discount?", default="")
    html = invoice_handler.generate(
        invoice_number, invoice_texts, user, project, discount
    )
    try:
        os.makedirs(os.path.join(settings.data_folder, "invoices"))
    except Exception as _:
        pass
    html_file = os.path.join(
        settings.data_folder, "invoices", f"{invoice_texts['title']}.html"
    )
    with open(html_file, "w") as f:
        f.write(html)
    console.print(f"The invoice is available in {html_file}")
    webbrowser.open(f"file:///{html_file}", autoraise=True)


@click.command()
def summary():
    """
    - shows summary of all projects.
    """
    data = data_handler.load_data()
    layout = Layout()

    count = 0
    left, right = [], []
    for project_name in data:
        project_data = data.get(project_name, {}).get("tasks", {})
        tree = Tree(
            f'[bold blue]{project_name}[/bold blue] ([i]{data.get(project_name, {})["status"]}[/i])'
        )
        if project_data == {}:
            tree.add("[red] No tasks yet. [/red]")
            right.append(Panel(tree, title=f"{project_name}"))
            continue
        duration = 0
        for task_name, t in project_data.items():
            task_duration = int(round(t["duration"]))
            duration += task_duration
            tree.add(
                f"[green]{task_name}[/green]: {get_duration_str(task_duration)} ([i]{t['status']}[/i])"
            )
        left.append(
            Panel(
                tree,
                title=f"{project_name}",
                subtitle=f"[blue bold]Total time[/blue bold]: {get_duration_str(duration)}",
                expand=False,
            )
        )
        count += 1
    layout.split_row(  # *p)
        Layout(name="left", size=45),
        Layout(name="right", size=55),
    )
    layout["left"].split_column(*left)
    layout["right"].split_column(*right)
    console.print(layout)


cli.add_command(init)
cli.add_command(project)
cli.add_command(task)
cli.add_command(show)
cli.add_command(config)
cli.add_command(invoice)
cli.add_command(summary)

if __name__ == "__main__":
    cli()
