import requests
from bs4 import BeautifulSoup
from core.product import Product


def scrape_cottonon_store(url: str, keywords: list[str], max_price: float = None) -> list[Product]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    cottonon_product = soup.find_all("div", class_="product-tile")
    seen_names = set()
    matches = []
    
    for product in cottonon_product:
        name_tag = product.find("a", class_="name-link")
        name = name_tag.get_text(strip=True) if name_tag else ""

        if name in seen_names:
            continue
        
        link_tag = product.find("a", href = True)
        link = link_tag.get("href") if link_tag else ""
 
        original_price = product.find("span", class_="product-standard-price")
        sale_price = product.find("span", class_="product-sales-price")

        original_price = extract_price(original_price) or extract_price(sale_price)
        sale_price = extract_price(sale_price)

        
        for kw in keywords:
            if kw.lower() in name.lower():
                seen_names.add(name)
                co_product = Product(
                    name=name,
                    sale_price=sale_price,
                    original_price=original_price,
                    discount_percentage="1",
                    store="Cotton On",
                    link=link
                )
                matches.append(co_product)
                break
    
    return matches



def extract_price(tag) -> float:
    if not tag:
        return None
    text = tag.get_text(strip=True).replace("AUD", "").replace("$", "").strip()
    try:
        return float(text)
    except ValueError:
        return None
    

