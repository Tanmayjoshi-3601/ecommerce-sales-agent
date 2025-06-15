import json
from typing import TypedDict, List
from pathlib import Path


class Product(TypedDict):
    title: str
    price: float
    rating: float
    reviews: int

def search_products(query: str) -> List[Product]:

    ## load dummy product data
    data_path = Path(__file__).parent.parent / "data/dummy_products.json"
    with open(data_path,"r") as f:
        products = json.load(f)
    
    # filter products by query keyword
    filtered = [p for p in products if query.lower() in p["title"].lower()]
    return filtered if filtered else products[:3] # fallback


