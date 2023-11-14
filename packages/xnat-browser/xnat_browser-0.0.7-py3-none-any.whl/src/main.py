""" CLI """
import logging
from pathlib import Path

import typer
import rich.traceback
import rich.logging

from src.browse_app import XnatBrowser
from src.query_app import XnatQuery

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.command()
def browse(server: str,
           verbose: bool = typer.Option(False, '--verbose', '-v')) -> None:
    XnatBrowser(server, logging.DEBUG if verbose else logging.INFO).run()


@app.command()
def query(server: str,
          search: Path = typer.Option(None, '--search', '-s', help='Search to load at startup'),
          verbose: bool = typer.Option(False, '--verbose', '-v')) -> None:
    XnatQuery(server, logging.DEBUG if verbose else logging.INFO, search=search).run()


if __name__ == "__main__":
    rich.traceback.install(width=None, word_wrap=True)
    app()
