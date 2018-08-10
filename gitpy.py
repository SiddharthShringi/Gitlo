import requests
import click


@click.group()
def cli():
    """ Main function in which all subcommand will be nested"""
    pass


@cli.command()
@cli.option()
def user(username):
    r = requests.get
