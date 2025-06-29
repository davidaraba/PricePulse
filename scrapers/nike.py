import requests
from bs4 import BeautifulSoup

def scrape_nike_store(url: str, keywords: list[str]) -> list[dict]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    name_tags = soup.find_all("div", class_="product-card__title")
    matches = []

    for tag in name_tags:
        name = tag.get_text(strip=True)
        for kw in keywords:
            if kw.lower() in name.lower():
                matches.append({
                    "name" : name,
                    "tag" : tag
                })
    return matches