import sys
import click

@click.group()
def cli():
    pass

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)


@click.command()
@click.option('--shout', is_flag=True, help="Shout the system name.")
def info(shout):
    """Info of your system."""
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!!!!'
    click.echo(rv)


cli.add_command(hello)
cli.add_command(info)

if __name__ == '__main__':
    cli()