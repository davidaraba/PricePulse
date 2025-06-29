import requests
from bs4 import BeautifulSoup

def scrape_nike_store(url: str) -> list[str]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    name_tags = soup.find_all("div", class_="product-card__title")

    names = [tag.get_text(strip = True) for tag in name_tags]
    return names