import click

@click.command()
@click.option("-c", "--config")
def generate(*args, **kwargs):
    from nft_generator.generator.generator import generate

    generate(*args, **kwargs)

    