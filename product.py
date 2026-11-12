from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def update_stock(self, quantity):
        if quantity < 0:
            print("Quantity must be 0 or more")
            return False
        self.__stock = quantity
        return True

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    @abstractmethod
    def get_fulfilment_info(self):
        pass

if __name__ == "__main__":
    p = Product("P999", "Mystery", 10.0, 1)

        

        

