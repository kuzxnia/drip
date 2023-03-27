from typer import Typer


cli = Typer()


@cli.command()
def init():
    ...

@cli.command()
def install():
    ...

@cli.command()
def add(package: str):
    ...


@cli.command()
def update():
    ...


@cli.command()
def remove():
    ...

@cli.command()
def search():
    ...
