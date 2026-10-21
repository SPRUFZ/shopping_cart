from datetime import date

# Store inventory
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

# customer cart and quantities
shopping_cart = []
quantities = []


def display_products():
    # show all products and prices
    print("\n========== AVAILABLE PRODUCTS ==========")
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]:<10} ${prices[i]:.2f}")


def find_price(product_name):
    # find the matching price for a product
    for i in range(len(products)):
        if products[i] == product_name:
            return prices[i]
    return 0.0


def add_product():
    # add a product to the cart or increase its quantity
    display_products()

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

    product_name = products[product_number - 1]

    if product_name in shopping_cart:
        index = shopping_cart.index(product_name)
        quantities[index] += 1
        print(f"{product_name} quantity increased to {quantities[index]}!")
    else:
        shopping_cart.append(product_name)
        quantities.append(1)
        print(f"{product_name} was added to your cart!")


def remove_product():
    # remove one item or lower its quantity.
    if not shopping_cart:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
        return

    print("\n========== YOUR SHOPPING CART ==========")
    for i in range(len(shopping_cart)):
        print(f"{i + 1}. {shopping_cart[i]} - Quantity: {quantities[i]}")

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

    index = item_number - 1
    product_name = shopping_cart[index]

    if quantities[index] > 1:
        quantities[index] -= 1
        print(f"One {product_name} was removed!")
        print(f"{product_name} quantity is now {quantities[index]}.")
    else:
        del shopping_cart[index]
        del quantities[index]
        print(f"{product_name} was removed from your cart!")


def calculate_total():
    # Add up the full cart total.
    total = 0.0
    for i in range(len(shopping_cart)):
        total += find_price(shopping_cart[i]) * quantities[i]
    return total


def view_cart():
    # Show cart items and subtotal
    if not shopping_cart:
        print("Your shopping cart is empty!")
        return

    print("\n========== YOUR SHOPPING CART ==========")
    print(f"{'Product':<10} {'Price':>8} {'Quantity':>9} {'Total':>10}")

    total_items = 0
    for i in range(len(shopping_cart)):
        price = find_price(shopping_cart[i])
        line_total = price * quantities[i]
        total_items += quantities[i]
        print(f"{i + 1}. {shopping_cart[i]:<10} ${price:>6.2f} {quantities[i]:>9} ${line_total:>8.2f}")

    print(f"\nTotal Items: {total_items}")
    print(f"Subtotal: ${calculate_total():.2f}")


def current_total():
    # Show the current subtotal without checkout
    if not shopping_cart:
        print("Your shopping cart is empty!")
        return

    print("\n========== CURRENT TOTAL ==========")
    subtotal = 0.0

    for i in range(len(shopping_cart)):
        price = find_price(shopping_cart[i])
        line_total = price * quantities[i]
        subtotal += line_total
        print(f"{shopping_cart[i]:<10} ${line_total:>7.2f}")

    print(f"\nSubtotal: ${subtotal:.2f}")


def calculate_discount(subtotal):
    # Decide discount based on subtotal
    if subtotal < 10:
        discount_rate = 0.00
    elif subtotal < 20:
        discount_rate = 0.05
    elif subtotal < 40:
        discount_rate = 0.10
    else:
        discount_rate = 0.15

    amount_saved = subtotal * discount_rate
    return discount_rate, amount_saved


def checkout():
    # Finish the purchase and show receipt
    if not shopping_cart:
        print("Your shopping cart is empty!")
        print("You cannot check out.")
        return

    subtotal = calculate_total()
    discount_rate, amount_saved = calculate_discount(subtotal)
    final_total = subtotal - amount_saved

    print("\n========== RECEIPT ==========")
    print(f"Date: {date.today().strftime('%m/%d/%Y')}")
    print()

    for i in range(len(shopping_cart)):
        price = find_price(shopping_cart[i])
        line_total = price * quantities[i]
        print(f"{shopping_cart[i]:<10} ${line_total:>8.2f}")

    print(f"\nSubtotal:       ${subtotal:.2f}")
    print(f"Discount:       {discount_rate * 100:.0f}%")
    print(f"Amount Saved:   ${amount_saved:.2f}")
    print(f"Final Total:    ${final_total:.2f}")
    print("\nThank you for shopping!")

    shopping_cart.clear()
    quantities.clear()


def show_menu():
    # Show the main menu
    print("\n========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")


def main():
    # Kep the program running until checkout
    while True:
        show_menu()

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
            view_cart()
        elif choice == 5:
            current_total()
        elif choice == 6:
            checkout()
            break


main()