import click


@click.group("trackalot")
def main():
    pass


from .server import cli # noqa
