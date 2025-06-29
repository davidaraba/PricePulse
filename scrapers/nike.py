import requests
from bs4 import BeautifulSoup
from core.product import Product

def scrape_nike_store(url: str, keywords: list[str], max_price: float = None) -> list[Product]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    product_cards = soup.find_all("div", class_="product-card")
    matches = []

    for card in product_cards:
        # print(tag.prettify())
        # break
        name_tag = card.find("div", class_="product-card__title")
        name = name_tag.get_text(strip=True) if name_tag else ""

        link_tag = card.find("a", href = True)
        
        if link_tag:
            link = link_tag.get("href")
        else:
            link = ""

        original_price = card.find("div", class_="product-price au__styling is--striked-out css-0")
        sale_price = card.find("div", class_= "product-price is--current-price css-1mj7kho")
        
        sale_price = float(sale_price.get_text(strip=True).replace("$", "")) if sale_price else None 
        original_price = float(original_price.get_text(strip=True).replace("$", "")) if original_price else sale_price

        if not in_budget(sale_price, max_price):
            continue

        discount = round((1 - sale_price / original_price) * 100) if sale_price and original_price and sale_price < original_price else 0

        
        for kw in keywords:
            if kw.lower() in name.lower():
                product = Product(
                    name=name,
                    sale_price=sale_price,
                    original_price=original_price,
                    discount_percentage=discount,
                    store="Nike",
                    link=link
                )
                matches.append(product)
                break 
    return matches

def in_budget(price, max_price) -> bool:
    if max_price is None:
        return True
    return price <= max_price