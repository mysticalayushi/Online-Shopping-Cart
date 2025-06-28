# Initializing Products and Cart

import json

catalog = [
    {
        "type": "physical",
        "product_id": "P001",
        "name": "Mechanical Keyboard",
        "price": 2499.0,
        "quantity_available": 10,
        "weight": 1.2
    },
    {
        "type": "digital",
        "product_id": "D001",
        "name": "Premium Software License",
        "price": 599.0,
        "quantity_available": 50,
        "download_link": "https://example.com/license"
    }
]

cart = []

with open("products.json", "w") as f:
    json.dump(catalog, f, indent=4)

with open("cart.json", "w") as f:
    json.dump(cart, f, indent=4)

print("Catalog and cart initialized.")
