import typer
from rich import print

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def init(path: str = ""):
    """Launch kanban ultimate for markdown"""
    print("entrando a la app")


def run():
    app()
