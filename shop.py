from datetime import date

products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]
shopping_cart = []
quantities = []


def display_products():
    """Display all available inventory items with prices."""
    print("\n========== AVAILABLE PRODUCTS ==========")
    for index in range(len(products)):
        print(f"{index + 1}. {products[index]:<10} ${prices[index]:.2f}")


def add_product():
    """Add a product to the cart and update quantity if it already exists."""
    while True:
        try:
            product_number = int(input("\nEnter product number: "))
        except ValueError:
            print("Invalid product!")
            print("Please choose a number between 1 and 6.")
            continue

        if product_number < 1 or product_number > len(products):
            print("Invalid product!")
            print("Please choose a number between 1 and 6.")
            continue

        break

    chosen_product = products[product_number - 1]

    if chosen_product in shopping_cart:
        position = shopping_cart.index(chosen_product)
        quantities[position] += 1
        print(f"{chosen_product} quantity increased to {quantities[position]}!")
    else:
        shopping_cart.append(chosen_product)
        quantities.append(1)
        print(f"{chosen_product} was added to your cart!")


def remove_product():
    """Remove one item from the cart or reduce quantity by one."""
    if not shopping_cart:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
        return

    print("\n========== YOUR SHOPPING CART ==========")
    for index in range(len(shopping_cart)):
        print(f"{index + 1}. {shopping_cart[index]:<10} - Quantity: {quantities[index]}")

    while True:
        try:
            item_number = int(input("\nWhich item would you like to remove? "))
        except ValueError:
            print("That item does not exist in your cart!")
            continue

        if item_number < 1 or item_number > len(shopping_cart):
            print("That item does not exist in your cart!")
            continue

        break

    selected_index = item_number - 1
    selected_product = shopping_cart[selected_index]

    if quantities[selected_index] > 1:
        quantities[selected_index] -= 1
        print(f"One {selected_product} was removed!")
        print(f"{selected_product} quantity is now {quantities[selected_index]}.")
    else:
        del shopping_cart[selected_index]
        del quantities[selected_index]
        print(f"{selected_product} was removed from your cart!")


def calculate_total():
    """Calculate the subtotal for all items in the cart using quantities."""
    subtotal = 0.0
    for index in range(len(shopping_cart)):
        product_name = shopping_cart[index]
        product_price = prices[products.index(product_name)]
        subtotal += product_price * quantities[index]
    return subtotal


def display_cart():
    """Display the current cart with product price, quantity, and line total."""
    if not shopping_cart:
        print("Your shopping cart is empty!")
        return

    print("\n========== YOUR SHOPPING CART ==========")
    print(f"{'Product':<10} {'Price':>9} {'Quantity':>9} {'Total':>10}")
    total_items = 0

    for index in range(len(shopping_cart)):
        product_name = shopping_cart[index]
        product_price = prices[products.index(product_name)]
        product_total = product_price * quantities[index]
        total_items += quantities[index]
        print(f"{index + 1}. {product_name:<10} ${product_price:>6.2f} {quantities[index]:>9} ${product_total:>8.2f}")

    print(f"\nTotal Items: {total_items}")
    print(f"Subtotal: ${calculate_total():.2f}")


def calculate_discount(subtotal):
    """Return the discount percentage and amount saved for the subtotal."""
    if subtotal < 10:
        discount_rate = 0
    elif subtotal < 20:
        discount_rate = 0.05
    elif subtotal < 40:
        discount_rate = 0.10
    else:
        discount_rate = 0.15

    amount_saved = subtotal * discount_rate
    return discount_rate, amount_saved


def print_receipt(subtotal, discount_rate, amount_saved, final_total):
    """Display the final receipt with the current date."""
    today = date.today().strftime("%m/%d/%Y")
    print("\n========== RECEIPT ==========")
    print(f"Date: {today}")
    print()

    for index in range(len(shopping_cart)):
        product_name = shopping_cart[index]
        product_price = prices[products.index(product_name)]
        product_total = product_price * quantities[index]
        print(f"{product_name:<10} ${product_total:>8.2f}")

    print(f"\nSubtotal:       ${subtotal:.2f}")
    print(f"Discount:       {discount_rate * 100:.0f}%")
    print(f"Amount Saved:   ${amount_saved:.2f}")
    print(f"Final Total:    ${final_total:.2f}")
    print("\nThank you for shopping!")


def checkout():
    """Process the final checkout and display the receipt."""
    if not shopping_cart:
        print("Your shopping cart is empty!")
        print("You cannot check out with no items.")
        return False

    subtotal = calculate_total()
    discount_rate, amount_saved = calculate_discount(subtotal)
    final_total = subtotal - amount_saved

    print("\n========== CHECKOUT ==========")
    print(f"Subtotal:       ${subtotal:.2f}")
    print(f"Discount:       {discount_rate * 100:.0f}%")
    print(f"Amount Saved:   ${amount_saved:.2f}")
    print(f"Final Total:    ${final_total:.2f}")
    print("\nThank you for shopping!")

    print_receipt(subtotal, discount_rate, amount_saved, final_total)
    return True


def display_current_total():
    """Show the subtotal and all current items in the cart."""
    if not shopping_cart:
        print("Your shopping cart is empty!")
        return

    print("\n========== CURRENT TOTAL ==========")
    subtotal = 0.0

    for index in range(len(shopping_cart)):
        product_name = shopping_cart[index]
        product_price = prices[products.index(product_name)]
        product_total = product_price * quantities[index]
        subtotal += product_total
        print(f"{product_name:<10} ${product_total:>7.2f}")

    print(f"\nSubtotal: ${subtotal:.2f}")


def show_main_menu():
    """Display the main program menu."""
    print("\n========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")


def main():
    while True:
        show_main_menu()

        while True:
            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid option!")
                continue

            if choice < 1 or choice > 6:
                print("Invalid option!")
                continue

            break

        if choice == 1:
            display_products()
        elif choice == 2:
            add_product()
        elif choice == 3:
            remove_product()
        elif choice == 4:
            display_cart()
        elif choice == 5:
            display_current_total()
        elif choice == 6:
            if checkout():
                break


if __name__ == "__main__":
    main()
