class CartItem:
    def __init__(self, product, quantity: int):
        self._product = product
        self._quantity = quantity

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self._quantity = value
        else:
            raise ValueError("Cart quantity cannot be negative.")

    def calculate_subtotal(self) -> float:
        return self._product.price * self._quantity

    def __str__(self):
        return f"{self._product.name} x {self._quantity} = ₹{self.calculate_subtotal()}"

    def to_dict(self) -> dict:
        return {
            "product_id": self._product.product_id,
            "quantity": self._quantity
        }
