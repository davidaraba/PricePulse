from core.store_loader import load_store_data
from scrapers.nike import scrape_nike_store
from scrapers.cottonon import scrape_cottonon_store
from core.alert_sender import send_sms
import time

start = time.time()

store_scrapers = {
    "Nike" : scrape_nike_store,
    "Cotton On" : scrape_cottonon_store
}

store_list = load_store_data("store_list.json")

for store in store_list:
    name = store["name"]
    url = store["url"]
    keywords = store["keywords"]
    scraper = store_scrapers.get(name)

    if scraper:
        matches = scraper(url, keywords, max_price=None)
        if matches:
            message_lines = [] 
            for match in matches:
                message_lines.append(
                    f"🎯 {match.name}\n"
                    f"💲 ${match.sale_price} ({match.discount_percentage}% off)\n"
                    f"🔗 {match.link}\n"
                )
            full_message = "\n".join(message_lines)
            # send_sms(full_message)
            print(full_message)
            
end = time.time()
print(f"⏱️ Runtime: {round(end - start, 2)} seconds")