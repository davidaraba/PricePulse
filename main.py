from core.store_loader import load_store_data
import requests

stores = load_store_data("store_list.json")

for store in stores:
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(store["url"], headers=headers, timeout=10)
        print(response.status_code)
    except Exception as e:
        print(f"❌ Failed to fetch {store['name']} - {e}")
    print("🛒 Store:", store["name"])
    print("🔗 URL:", store["url"])
    print("🎯 Keywords:", store["keywords"])
    print("-" * 40)