# -*- coding: utf-8 -*-

import click


@click.group()
def main():
    pass

from nft_generator.command.version import version
from nft_generator.command.generate import generate

main.add_command(version)
main.add_command(generate)

if __name__ == "__main__":
    main()
