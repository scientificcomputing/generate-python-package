"""Console script for {{cookiecutter.module_name}}."""
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse


def main():
    """Console script for {{cookiecutter.module_name}}."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into {{cookiecutter.module_name}}.cli.main")
    return 0
{%- elif cookiecutter.command_line_interface|lower == 'click' %}
import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def main(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")
    return 0
{%- elif cookiecutter.command_line_interface|lower == 'typer' %}
import typer


def main(count: int, name: str) -> int:
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        typer.echo(f"Hello {name}!")
    return 0
{% endif %}
