# -*- coding: utf-8 -*-

import click


@click.group()
def main():
    pass

from nft_generator.command.version import version

main.add_command(version)

if __name__ == "__main__":
    main()
