import json
import os
from product import Product, PhysicalProduct, DigitalProduct
from cart_item import CartItem


class ShoppingCart:
    # Skeleton Class
    def __init__(self, product_catalog_file='products.json', cart_state_file='cart.json'):
        self._items = {}  # product_id: CartItem
        self._product_catalog_file = product_catalog_file
        self._cart_state_file = cart_state_file
        self._catalog = self._load_catalog()
        self._load_cart_state()

    # Fetching Data and Rebuilding Catalog
    def _load_catalog(self):
        if not os.path.exists(self._product_catalog_file):
            return {}

        with open(self._product_catalog_file, 'r') as f:
            raw_data = json.load(f)

        catalog = {}
        for item in raw_data:
            ptype = item.get("type")
            if ptype == "physical":
                prod = PhysicalProduct(item["product_id"], item["name"], item["price"], item["quantity_available"],
                                       item["weight"])
            elif ptype == "digital":
                prod = DigitalProduct(item["product_id"], item["name"], item["price"], item["quantity_available"],
                                      item["download_link"])
            else:
                prod = Product(item["product_id"], item["name"], item["price"], item["quantity_available"])
            catalog[prod.product_id] = prod
        return catalog

    # Cart State Loading

    def _load_cart_state(self):
        if not os.path.exists(self._cart_state_file):
            return

        with open(self._cart_state_file, 'r') as f:
            raw_cart = json.load(f)

        for item in raw_cart:
            pid = item["product_id"]
            qty = item["quantity"]
            if pid in self._catalog:
                cart_item = CartItem(self._catalog[pid], qty)
                self._items[pid] = cart_item

    # Saving Methods

    def _save_catalog(self):
        data = [p.to_dict() for p in self._catalog.values()]
        with open(self._product_catalog_file, 'w') as f:
            json.dump(data, f, indent=4)

    def _save_cart_state(self):
        data = [ci.to_dict() for ci in self._items.values()]
        with open(self._cart_state_file, 'w') as f:
            json.dump(data, f, indent=4)

    # Cart Functionalities Made

    def add_item(self, product_id, quantity):
        if product_id not in self._catalog:
            print("❌ Product not found.")
            return False

        product = self._catalog[product_id]
        if not product.decrease_quantity(quantity):
            print("❌ Not enough stock.")
            return False

        if product_id in self._items:
            self._items[product_id].quantity += quantity
        else:
            self._items[product_id] = CartItem(product, quantity)

        self._save_cart_state()
        self._save_catalog()
        print("✅ Item added to cart.")
        return True

    def remove_item(self, product_id):
        if product_id not in self._items:
            print("❌ Item not found in cart.")
            return False

        removed_item = self._items.pop(product_id)
        removed_item.product.increase_quantity(removed_item.quantity)

        self._save_cart_state()
        self._save_catalog()
        print("🗑️ Item removed from cart.")
        return True

    def update_quantity(self, product_id, new_quantity):
        if product_id not in self._items:
            print("❌ Item not in cart.")
            return False

        cart_item = self._items[product_id]
        current_quantity = cart_item.quantity
        product = cart_item.product

        # Stock adjustment
        if new_quantity > current_quantity:
            delta = new_quantity - current_quantity
            if not product.decrease_quantity(delta):
                print("❌ Not enough stock.")
                return False
        else:
            delta = current_quantity - new_quantity
            product.increase_quantity(delta)

        cart_item.quantity = new_quantity
        self._save_cart_state()
        self._save_catalog()
        print("🔁 Quantity updated.")
        return True

    # Display Method

    def display_cart(self):
        if not self._items:
            print("🛒 Cart is empty.")
            return
        print("\n📦 Your Shopping Cart:")
        for item in self._items.values():
            print(item)
        print(f"\n💰 Grand Total: ₹{self.get_total()}")

    def get_total(self):
        return sum(item.calculate_subtotal() for item in self._items.values())

    def display_products(self):
        print("\n🛍️ Available Products:")
        for product in self._catalog.values():
            print(product.display_details())
