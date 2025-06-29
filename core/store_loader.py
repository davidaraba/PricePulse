import json
import requests

def load_store_data(filename: str) -> list[dict]:
    with open(filename, "r") as file:
        return json.load(file)
    

