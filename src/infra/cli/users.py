import typer
from dependency_injector.wiring import inject

from src.config.containers import Container

app = typer.Typer()

container = Container()

@app.command()
@inject
def create(
    name: str = typer.Option(..., prompt=True),
    email: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True),
    ):
    pass
