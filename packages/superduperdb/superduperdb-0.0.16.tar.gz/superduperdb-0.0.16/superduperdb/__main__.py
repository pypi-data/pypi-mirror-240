import sys

import click

from .cli import app, config, info
from .cli.serve import local_cluster, serve

__all__ = 'config', 'info', 'local_cluster', 'serve'


def run():
    """
    Entrypoint for the CLI. This is the function that is called when the
    user runs `python -m superduperdb`.
    """
    try:
        app(standalone_mode=False)
    except click.ClickException as e:
        return f'{e.__class__.__name__}: {e.message}'
    except click.Abort:
        return 'Aborted'


if __name__ == '__main__':
    sys.exit(run())
