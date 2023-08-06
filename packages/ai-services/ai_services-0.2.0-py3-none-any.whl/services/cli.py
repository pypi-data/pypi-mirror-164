import os

import click
from rich.console import Console

from services.commands.web import webcli
from services.commands.manager import managercli
from services.commands.common import startproject


def init_cli():

    console = Console()

    @click.group()
    @click.pass_context
    def cli(ctx):
        """
        Command line tool
        """

    @click.command()
    def version():
        """Actual version"""
        from services.utils import get_version

        ver = get_version("__version__.py")
        console.print(f"[bold magenta]{ver}[/bold magenta]")

    cli.add_command(version)
    cli.add_command(webcli)
    cli.add_command(managercli)
    cli.add_command(startproject)
    return cli


cli = init_cli()

if __name__ == "__main__":

    cli()
