import sys
import click

from tdk.core import TurkishWord


@click.command()
@click.argument('term')
def run(term):
    """
    A command line tool to query meaning of Turkish word from official dictionary.
    """
    word = TurkishWord(input)
    word.query()
    output = word.meaning

    click.echo(output)


