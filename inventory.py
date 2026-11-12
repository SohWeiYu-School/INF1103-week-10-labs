from product import Product


class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def get_products(self) -> list[Product]:
        return self.__products

    def display_all_products(self) -> None:
        print("\nCurrent Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)
