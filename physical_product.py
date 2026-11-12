from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float,
                 stock_quantity: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.__weight: float = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.get_weight()} kg")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping"

    def calculate_shipping_cost(self) -> float:
        shipping = 5 + 2 * self.get_weight()
        return shipping


if __name__ == "__main__":
    supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
    guitar = PhysicalProduct("P010", "Guitar", 300.0, 5, supplier, 4.0)
    guitar.display_information()
    print(guitar.get_fulfilment_info())
    print(f"Shipping cost: ${guitar.calculate_shipping_cost():.2f}")
