import json
import os

PRODUCTS_FILE = "products.json"
CART_FILE = "cart.json"

def create_physical_product():
    product_id = input("Enter Product ID (e.g., P005): ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price (₹): "))
    quantity = int(input("Enter Stock Quantity: "))
    weight = float(input("Enter Weight (kg): "))
    return {
        "type": "physical",
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity_available": quantity,
        "weight": weight
    }

def create_digital_product():
    product_id = input("Enter Product ID (e.g., D002): ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price (₹): "))
    quantity = int(input("Enter Available Downloads: "))
    download_link = input("Enter Download Link URL: ")
    return {
        "type": "digital",
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity_available": quantity,
        "download_link": download_link
    }

def load_existing_products():
    if os.path.exists(PRODUCTS_FILE):
        try:
            with open(PRODUCTS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Warning: products.json is empty or invalid. Starting fresh.")
            return []
    return []

def main():
    print("🛍️ Product Catalog Bootstrap Tool (Append Mode)\n")

    products = load_existing_products()

    while True:
        print("\nChoose Product Type to Add:")
        print("1. Physical Product")
        print("2. Digital Product")
        print("3. Done Adding Products")
        choice = input("Enter choice: ")

        if choice == '1':
            product = create_physical_product()
            products.append(product)
        elif choice == '2':
            product = create_digital_product()
            products.append(product)
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice. Try again.")

    # Save updated product list
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products, f, indent=4)
    print(f"\n✅ Total products saved to {PRODUCTS_FILE}: {len(products)}")

    # Create empty cart.json only if it doesn’t exist
    if not os.path.exists(CART_FILE):
        with open(CART_FILE, "w") as f:
            json.dump([], f, indent=4)
        print(f"🧺 Initialized empty cart at {CART_FILE}")
    else:
        print(f"🧺 Cart already exists. Left unchanged.")

if __name__ == "__main__":
    main()
