import ast
import os
from pathlib import Path

import click

from archive_strategy.archiver import ArchivePolicy, ArchiveConfig, Archiver


@click.group()
def config():
    pass


@config.command()
def show_config():
    """Show the current configuration"""
    config = ArchiveConfig()
    config._show()


@click.group()
def information():
    pass


@information.command()
def show():
    """Show the current list of backups"""
    archive_config = ArchiveConfig()
    archiver = Archiver(config=archive_config)
    archiver.apply_policies_to_backups()
    archiver.list_backups()


@click.group()
def execution():
    pass


@execution.command()
@click.option(
    "--prune",
    is_flag=True,
    default=False,
    show_default=True,
    help="Determine whether to prune backup files that are no longer needed.",
)
@click.option(
    "--verbose",
    is_flag=True,
    default=False,
    show_default=True,
    help="Display additional information for debugging.",
)
def run(prune, verbose):
    """Run the archiver"""
    archive_config = ArchiveConfig(prune=prune, verbose=verbose)
    archiver = Archiver(config=archive_config)
    archiver.apply_policies_to_backups()
    archiver.archive()


cli = click.CommandCollection(sources=[config, information, execution])


def main():
    cli()
