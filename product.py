class Product:
    def __init__(self, product_id, name, price,
                 quantity_available):  
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_available = quantity_available

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity_available(self):
        return self._quantity_available

    @quantity_available.setter
    def quantity_available(self, value):
        if value >= 0:
            self._quantity_available = value
        else:
            raise ValueError("Quantity cannot be negative")

    def display_details(self):
        return f"{self._product_id}: {self._name} - ₹{self._price} [{self._quantity_available} in stock]"

    def decrease_quantity(self, amount):
        if amount <= self._quantity_available:
            self._quantity_available -= amount
            return True
        return False

    def increase_quantity(self, amount):
        self._quantity_available += amount

    # For Using in JSON to save the cart and the catalog data
    def to_dict(self):
        return {
            "type": "base",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity_available": self._quantity_available
        }


# Inherited Class With Product as parents with weight as new attribute

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, quantity_available: int, weight: float):
        super().__init__(product_id, name, price, quantity_available)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    def display_details(self) -> str:
        return f"{super().display_details()} | Weight: {self._weight} kg"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "type": "physical",
            "weight": self._weight
        })
        return data


# Inherited Class With Product as parents with download link as new attribute

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, quantity_available: int, download_link: str):
        super().__init__(product_id, name, price, quantity_available)
        self._download_link = download_link

    @property
    def download_link(self):
        return self._download_link

    def display_details(self) -> str:
        return f"ID: {self.product_id} | {self.name} | ₹{self.price} | Link: {self._download_link}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "type": "digital",
            "download_link": self._download_link
        })
        return data
