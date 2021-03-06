import click
import json
from src.config import Config
from src.console import Console
from src.fetch import Fetch
from src.history import History

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
config = Config()
console = Console()

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
# @cli.argument("--repo.user", '-ru', required=1)
# @cli.argument("--repo.name", '-rn', required=1)
def fetch(user, name):
# def fetch(user, name):


    if 'sites' in config:
        f = Fetch(config['sites'])

        for i in json.dumps(f._info, indent=4).split('\n'):
            console.info(i)

        h = History(f._info)
        h.execute()

    else:
        console.error("No sites to fetch")
