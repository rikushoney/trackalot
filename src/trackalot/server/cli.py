from trackalot import cli

from .takealot import Takealot


@cli.main.command()
def server():
    print(Takealot()._raw_product_details("PLID54494899"))
