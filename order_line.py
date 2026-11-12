from product import Product


class OrderLine:

    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity

    def display_information(self) -> None:
        print(f"{self.product.get_name()} x{self.quantity} = ${self.calculate_subtotal():.2f}")
