import requests
import click


@click.group()
def cli():
    """ Main function in which all subcommand will be nested"""
    pass


@cli.command()
@click.argument('username')
def user(username):
    r = requests.get('https://api.github.com/users/{}'.format(username)).json()
    print('Name: {}, Repos: {}, Bio: {}'.format(r['name'], r['public_repos'], r['bio']))


@cli.command()
@click.argument('username')
def repos(username):
    r = requests.get('https://api.github.com/users/{}/repos'.format(username)).json()
    for i in range(len(r)):
        print(r[i]['name'])
