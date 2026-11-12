from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float,
                 stock_quantity: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.get_download_size()} MB")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally via download link"

if __name__ == "__main__":
    supplier = Supplier("S002", "SoftWorld Distribution", "orders@softworld.com")
    windows = DigitalProduct("D001", "Windows 11", 199.0, 100, supplier, 5000)
    windows.display_information()
    print(windows.get_fulfilment_info())
