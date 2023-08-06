#!/usr/bin/env python3

import click
import requests
from rich.table import Table
from bs4 import BeautifulSoup
from rich.console import Console

console = Console()
baseurl = "https://www.pricerunner.dk"

banner = """[not italic][bold magenta]┌─┐┬─┐┬┌─┐┌─┐┬─┐┬ ┬┌┐┌┌┐┌┌─┐┬─┐   ┌─┐┬  ┬
├─┘├┬┘││  ├┤ ├┬┘│ │││││││├┤ ├┬┘───│  │  │
┴  ┴└─┴└─┘└─┘┴└─└─┘┘└┘┘└┘└─┘┴└─   └─┘┴─┘┴[/not italic][/bold magenta]"""


def extract_values(divelem):
    aa = divelem.find("a", {"target": "_blank"})
    uu = baseurl + divelem.find("a", {"target": "_blank"})["href"]
    link = f"[bold blue][link={uu}]{aa['aria-label']}[/link][/bold blue]"
    price = divelem.find("span", {"data-testid": "priceComponent"}).text
    stocktmp = divelem.find_all("use")[1]["href"][1:]
    if stocktmp[0] == "I":
        stock = f"[bold green]{stocktmp}[/bold green]"
    else:
        stock = f"[bold red]{stocktmp}[/bold red]"
    sni = divelem.find("button")["aria-label"]
    shopname = sni[sni.index("om") + 3 :]
    if shopname == "Proshop.dk":
        shopname = f"[bold green]{shopname}[/bold green]"
    return shopname, link, stock, price


def get_product_link(query):
    url = f"{baseurl}/public/search/suggest/dk?q={query}"
    try:
        producturl = f"{baseurl}{requests.get(url).json()['products'][0]['url']}"
    except:
        console.print("[bold red]Product not found[/bold red]")
        exit()
    return producturl


def find_price_items(query):
    purl = get_product_link(query)
    bs = BeautifulSoup(requests.get(purl).text, "html.parser")
    return bs.find_all("div", {"class": "foWwRfeBAj"})


def make_table(query):
    items = find_price_items(query)
    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.title = banner
    table.add_column("Shop Name")
    table.add_column("Link")
    table.add_column("Stock Status", justify="right")
    table.add_column("Price", justify="right")
    for item in items:
        shopname, link, stock, price = extract_values(item)
        table.add_row(shopname, link, stock, price)
    console.print(table)

@click.command()
@click.argument("search")
def cli(search:str):
    make_table(search)

if __name__ == "__main__":
    cli()
