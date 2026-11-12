from abc import ABC, abstractmethod

from supplier import Supplier


class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float,
                 stock_quantity: int, supplier: Supplier):
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock_quantity
        self.supplier: Supplier = supplier

    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def update_stock(self, quantity: int) -> bool:
        if quantity < 0:
            print("Quantity must be 0 or more")
            return False
        self.__stock = quantity
        return True

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
