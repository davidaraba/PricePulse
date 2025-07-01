import requests
from bs4 import BeautifulSoup
from core.product import Product


def scrape_cottonon_store(url: str, keywords: list[str], max_price: float = None) -> list[Product]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    cottonon_product = soup.find_all("div", class_="product-name")
    seen_names = set()
    matches = []
    
    for product in cottonon_product:
        name_tag = product.find("a", class_="name-link")
        name = name_tag.get_text(strip=True) if name_tag else ""

        if name in seen_names:
            continue
        
    
        for kw in keywords:
            if kw.lower() in name.lower():
                seen_names.add(name)
                cottonon_product = Product(
                    name=name,
                    sale_price="1",
                    original_price="1",
                    discount_percentage="1",
                    store="Cotton On",
                    link="david"
                )
                matches.append(cottonon_product)
                break
    
    return matches


