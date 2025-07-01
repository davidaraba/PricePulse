from core.product import Product
import requests
from bs4 import BeautifulSoup

def scrape_subtype_store (url: str, keywords: list[str], max_price: float = None) -> list[Product]:
    pass

response = requests.get("https://www.subtypestore.com/au/categories/sale/mens-sale/mens-sale-footwear?pid=nav-sale-mens")
print(response)