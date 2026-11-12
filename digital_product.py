from product import Product

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.get_download_size()} MB")

    def get_fulfilment_info(self):
        return "Delivered digitally via download link"

if __name__ == "__main__":
    windows = DigitalProduct("D001", "Windows 11", 199.0, 100, 5000)
    windows.display_information()
    print(windows.get_fulfilment_info())
