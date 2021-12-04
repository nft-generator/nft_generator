# -*- coding: utf-8 -*-

import click


@click.group()
def main():
    pass

@click.command()
def version():
    print(__version__)

if __name__ == "__main__":
    main()
