import requests
from bs4 import BeautifulSoup

def scrape_nike_store(url: str, keywords: list[str]) -> list[dict]:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    product_cards = soup.find_all("div", class_="product-card__info")
    matches = []

    for card in product_cards:
        # print(tag.prettify())
        # break
        name_tag = card.find("div", class_="product-card__title")
        name = name_tag.get_text(strip=True) if name_tag else ""
        
        original_price = card.find("div", class_="product-price au__styling is--striked-out css-0")
        sale_price = card.find("div", class_= "product-price is--current-price css-1mj7kho")

        if sale_price:
            sale_price = float(sale_price.get_text(strip=True).replace("$", ""))
        else:
            sale_price = None
        
        if original_price:
            original_price = float(original_price.get_text(strip=True).replace("$", ""))
        else:
            original_price = sale_price 

        if sale_price and original_price and sale_price < original_price:
            discount = round((1 - sale_price / original_price) * 100)
        else:
            discount = 0
        
        for kw in keywords:
            if kw.lower() in name.lower():
                matches.append({
                    "name" : name,
                    "original price" : original_price, 
                    "sale price" : sale_price,
                    "discount percentage" : discount,
                    "card" : card
                })
    return matches