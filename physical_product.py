from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.get_weight()} kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping"

    def calculate_shipping_cost(self):
        shipping = 5 + 2 * self.get_weight()
        return shipping


if __name__ == "__main__":
    guitar = PhysicalProduct("P010", "Guitar", 300.0, 5, 40)
    guitar.display_information()
    print(guitar.get_fulfilment_info())
    print(f"Shipping cost: ${guitar.calculate_shipping_cost():.2f}")

    cable = PhysicalProduct("P011", "USB Cable", 10.0, 50, 0.5)
    cable.display_information()
    print(f"Shipping cost: ${cable.calculate_shipping_cost():.2f}")

    
