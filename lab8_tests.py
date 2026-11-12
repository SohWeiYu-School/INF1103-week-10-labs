from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


# Section 2: Association
def test_association() -> None:
    print("Section 2: Association")
    supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
    laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.0)
    antivirus = DigitalProduct("D002", "Antivirus", 59.90, 200, supplier, 350)

    laptop.supplier.display_information()
    antivirus.supplier.display_information()

    del supplier
    print("After del supplier:")
    laptop.supplier.display_information()
    antivirus.supplier.display_information()


# Section 3: Aggregation
def test_aggregation() -> None:
    print("\nSection 3: Aggregation")
    supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
    mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, supplier, 1.0)
    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(mouse)
    inventory_a.remove_product("P002")
    print("Removed from Inventory A, product still works:")
    mouse.display_information()

    inventory_b.add_product(mouse)
    print("Added the same product to Inventory B:")
    inventory_b.display_all_products()


# Section 4: Composition
def test_composition() -> None:
    print("\nSection 4: Composition")
    supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
    keyboard = PhysicalProduct("P003", "Keyboard", 45.00, 25, supplier, 1.0)
    windows = DigitalProduct("D001", "Windows 11", 199.00, 100, supplier, 5000)

    order_1 = Order("O001")
    order_1.add_order_line(keyboard, 2)
    order_1.add_order_line(windows, 1)
    order_1.display_order()

    order_2 = Order("O002")
    order_2.add_order_line(keyboard, 5)
    line_1 = order_1.order_lines[0]
    line_2 = order_2.order_lines[0]
    print(f"Same OrderLine object: {line_1 is line_2}")
    print(f"Same Product object: {line_1.product is line_2.product}")

    order_1.remove_order_line("D001")
    print("After removing Windows 11 from O001:")
    order_1.display_order()


# Section 6: Liskov Substitution
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_lsp() -> None:
    print("\nSection 6: Liskov Substitution")
    supplier = Supplier("S002", "SoftWorld Distribution", "orders@softworld.com")
    physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.0)
    digital = DigitalProduct("D001", "Windows 11", 199.00, 100, supplier, 5000)

    show_product_details(physical)
    show_product_details(digital)

    inventory = Inventory()
    inventory.add_product(physical)
    inventory.add_product(digital)
    inventory.display_all_products()


# Section 7: Polymorphism
def test_polymorphism() -> None:
    print("\nSection 7: Polymorphism")
    supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
    inventory = Inventory()
    inventory.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.0))
    inventory.add_product(DigitalProduct("D001", "Windows 11", 199.00, 100, supplier, 5000))

    for product in inventory.get_products():
        product.display_information()
        print(product.get_fulfilment_info())


if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp()
    test_polymorphism()
