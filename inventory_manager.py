"""
INF1103 Week 9 (Lab 7) - Inventory Management System (Inheritance, Abstraction, Interfaces)
"""

import json
import os

from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


INVENTORY_FILE = "inventory.json"


def load_default_products(inventory):
    inventory.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0))
    inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, 3.0))
    inventory.add_product(PhysicalProduct("P003", "Keyboard", 45.00, 25, 5.5))
    inventory.add_product(DigitalProduct("D001", "Windows 11", 199.00, 100, 5000))


def load_inventory(inventory):
    if os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} found.")
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)
        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"])
            elif item["type"] == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["download_size"])
            inventory.add_product(product)
        print("Inventory loaded successfully.")
    else:
        print(f"{INVENTORY_FILE} not found. Starting with default inventory.")
        load_default_products(inventory)


def save_inventory(inventory):
    print("\nSaving inventory...")
    data = []
    for product in inventory.get_products():
        item = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),
        }
        if isinstance(product, PhysicalProduct):
            item["type"] = "physical"
            item["weight"] = product.get_weight()
        elif isinstance(product, DigitalProduct):
            item["type"] = "digital"
            item["download_size"] = product.get_download_size()
        data.append(item)
    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Inventory saved successfully to {INVENTORY_FILE}.")


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    product_type = input("Type (physical/digital): ").strip().lower()

    if product_type == "physical":
        weight = float(input("Weight (kg): "))
        product = PhysicalProduct(product_id, name, price, stock, weight)
    elif product_type == "digital":
        download_size = float(input("Download Size (MB): "))
        product = DigitalProduct(product_id, name, price, stock, download_size)
    else:
        print("Invalid type. Please enter 'physical' or 'digital'.")
        return

    inventory.add_product(product)
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print(f"Product Found:\nName: {product.get_name()}\nCurrent Stock: {product.get_stock()}")
    quantity = int(input("New Stock Quantity: "))
    if product.update_stock(quantity):
        print("Stock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("-" * 48)
    product.display_information()
    print("-" * 48)


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()
