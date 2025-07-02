from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.product import Product
from typing import List

def scrape_subtype_store(url: str, keywords: list[str], max_price: float = None) -> List[Product]:
    options = Options()
    options.add_argument("--headless")  # run browser in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://google.com")

    matches = []

    # driver.quit()
    return matches
