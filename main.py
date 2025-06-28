from shopping_cart import ShoppingCart


def main():
    cart = ShoppingCart()
    while True:
        print("\n" + "-" * 50)
        print(" ONLINE SHOPPING CART")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Quantity")
        print("5. Remove Item")
        print("6. Checkout (Under progress)")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            cart.display_products()
        elif choice == '2':
            pid = input("Enter Product ID: ")
            qty = int(input("Enter Quantity: "))
            cart.add_item(pid, qty)
        elif choice == '3':
            cart.display_cart()
        elif choice == '4':
            pid = input("Product ID to update: ")
            new_qty = int(input("New Quantity: "))
            cart.update_quantity(pid, new_qty)
        elif choice == '5':
            pid = input("Product ID to remove: ")
            cart.remove_item(pid)
        elif choice == '6':
            print("🧾 (Pretend checkout) Thank you for shopping!")
            break
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
