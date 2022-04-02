import click
from io import BytesIO
import requests
from zipfile import ZipFile


@click.command()
@click.argument('type')
@click.argument('name')
def action(type, name):
    if type == "install":
        click.echo(f"Downloading {name}...")
        content = requests.get(name)

        with ZipFile(BytesIO(content.content)) as zfile:
            zfile.extractall('testdownload/')

        click.echo(f"Downloaded {name}")
    elif type == "uninstall":
        click.echo(f"Uninstalling {name}...")
        click.echo(f"Uninstalled {name}")
    else:
        raise Exception(f"type {type} not found. Type --help for usage")


if __name__ == "__main__":
    action()
