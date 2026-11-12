import json
import os

from inventory import Inventory
from order import Order
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


INVENTORY_FILE = "inventory.json"


def load_default_products(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    techsource = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
    softworld = Supplier("S002", "SoftWorld Distribution", "orders@softworld.com")
    suppliers["S001"] = techsource
    suppliers["S002"] = softworld
    inventory.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 15, techsource, 2.0))
    inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, techsource, 1.0))
    inventory.add_product(PhysicalProduct("P003", "Keyboard", 45.00, 25, techsource, 1.0))
    inventory.add_product(DigitalProduct("D001", "Windows 11", 199.00, 100, softworld, 5000))


def load_inventory(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    if os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} found.")
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)
        for item in data["suppliers"]:
            suppliers[item["id"]] = Supplier(item["id"], item["name"], item["email"])
        for item in data["products"]:
            supplier = suppliers[item["supplier_id"]]
            product: Product
            if item["type"] == "physical":
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], supplier, item["weight"])
            else:
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], supplier, item["download_size"])
            inventory.add_product(product)
        print("Inventory loaded successfully.")
    else:
        print(f"{INVENTORY_FILE} not found. Starting with default inventory.")
        load_default_products(inventory, suppliers)


def save_inventory(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    print("\nSaving inventory...")
    supplier_data = []
    for supplier in suppliers.values():
        supplier_data.append({
            "id": supplier.get_supplier_id(),
            "name": supplier.get_name(),
            "email": supplier.get_contact_email(),
        })
    product_data = []
    for product in inventory.get_products():
        item: dict[str, str | float | int] = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),
            "supplier_id": product.supplier.get_supplier_id(),
        }
        if isinstance(product, PhysicalProduct):
            item["type"] = "physical"
            item["weight"] = product.get_weight()
        elif isinstance(product, DigitalProduct):
            item["type"] = "digital"
            item["download_size"] = product.get_download_size()
        product_data.append(item)
    with open(INVENTORY_FILE, "w") as f:
        json.dump({"suppliers": supplier_data, "products": product_data}, f, indent=4)
    print(f"Inventory saved successfully to {INVENTORY_FILE}.")


def add_product(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    supplier_id = input(f"Supplier ID ({', '.join(suppliers)}): ")
    if supplier_id not in suppliers:
        print("Supplier not found.")
        return
    supplier = suppliers[supplier_id]
    product_type = input("Type (physical/digital): ").strip().lower()

    product: Product
    if product_type == "physical":
        weight = float(input("Weight (kg): "))
        product = PhysicalProduct(product_id, name, price, stock, supplier, weight)
    elif product_type == "digital":
        download_size = float(input("Download Size (MB): "))
        product = DigitalProduct(product_id, name, price, stock, supplier, download_size)
    else:
        print("Invalid type. Please enter 'physical' or 'digital'.")
        return

    inventory.add_product(product)
    print("Product added successfully!")


def update_stock(inventory: Inventory) -> None:
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print(f"Product Found:\nName: {product.get_name()}\nCurrent Stock: {product.get_stock()}")
    quantity = int(input("New Stock Quantity: "))
    if product.update_stock(quantity):
        print("Stock updated successfully!")


def search_product(inventory: Inventory) -> None:
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("-" * 48)
    product.display_information()
    product.supplier.display_information()
    print("-" * 48)


def create_order(inventory: Inventory) -> None:
    print("\nCreate Order")
    order = Order(input("Order ID: "))
    while True:
        product_id = input("Product ID (blank to finish): ")
        if product_id == "":
            break
        product = inventory.find_product(product_id)
        if product is None:
            print("Product not found.")
            continue
        quantity = int(input("Quantity: "))
        order.add_order_line(product, quantity)
    order.display_order()


def main() -> None:
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = Inventory()
    suppliers: dict[str, Supplier] = {}
    load_inventory(inventory, suppliers)

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Create Order")
        print("6. Save Inventory")
        print("7. Exit")
        print("----------------------------")

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all_products()
        elif option == "2":
            add_product(inventory, suppliers)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            create_order(inventory)
        elif option == "6":
            save_inventory(inventory, suppliers)
        elif option == "7":
            print("\nSaving inventory before exit...")
            save_inventory(inventory, suppliers)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-7.")


if __name__ == "__main__":
    main()
