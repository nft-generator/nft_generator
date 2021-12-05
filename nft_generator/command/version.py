import click

from nft_generator import __version__

@click.command()
def version():
    print(__version__)

    