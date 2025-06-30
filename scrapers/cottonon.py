import requests
from bs4 import BeautifulSoup
from core.product import Product


def scrape_cottonon_store(url: str, keywords: list[str], max_price: float = None) -> list[Product]:
    pass