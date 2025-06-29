from dataclasses import dataclass

@dataclass
class Product:
    name: str
    sale_price: float
    original_price: float
    discount_percentage: float
    store: str
    link: str
