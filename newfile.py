# 🍔 Simple Online Food Ordering Simulation

# --- 1. Data Structures (Database Simulation) ---
MENU = {
    1: {"name": "Burger", "price": 8.99},
    2: {"name": "Pizza (Slice)", "price": 4.50},
    3: {"name": "Fries", "price": 2.99},
    4: {"name": "Soda", "price": 1.50},
    5: {"name": "Milkshake", "price": 4.00}
}

user_cart = []
order_history = []

# --- 2. Core Functions ---

def display_menu():
    """Prints the available menu items."""
    print("\n--- 📝 Our Menu ---")
    print("ID | Item Name | Price")
    print("---|-----------|-------")
    for item_id, item_details in MENU.items():
        print(f"{item_id:<2} | {item_details['name']:<9} | ${item_details['price']:.2f}")
    print("-------------------")

def add_to_cart(item_id, quantity):
    """Adds a specified item and quantity to the user's cart."""
    try:
        item_id = int(item_id)
        quantity = int(quantity)
        if item_id in MENU and quantity > 0:
            item = MENU[item_id]
            user_cart.append({
                "item_id": item_id,
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity
            })
            print(f"✅ Added {quantity} x {item['name']} to your cart.")
        else:
            print("❌ Invalid Item ID or Quantity. Please try again.")
    except ValueError:
        print("❌ Invalid input. ID and Quantity must be numbers.")

def view_cart():
    """Prints the current contents of the user's cart and the total."""
    if not user_cart:
        print("\n🛒 Your cart is currently empty.")
        return 0

    print("\n--- 🛒 Your Shopping Cart ---")
    total_cost = 0.0
    for item in user_cart:
        subtotal = item["price"] * item["quantity"]
        total_cost += subtotal
        print(f"* {item['quantity']} x {item['name']} @ ${item['price']:.2f} each = ${subtotal:.2f}")

    # Simple tax calculation
    TAX_RATE = 0.08
    tax_amount = total_cost * TAX_RATE
    final_total = total_cost + tax_amount

    print("-----------------------------")
    print(f"Subtotal: ${total_cost:.2f}")
    print(f"Tax ({TAX_RATE*100}%):  ${tax_amount:.2f}")
    print(f"**Total:  ${final_total:.2f}**")
    print("-----------------------------")
    return final_total

def checkout():
    """Finalizes the order, moves cart items to history, and clears the cart."""
    global user_cart, order_history

    if not user_cart:
        print("\n🚫 Cannot checkout. Your cart is empty.")
        return

    final_cost = view_cart()

    print("\n--- 💳 Checkout Process ---")
    confirmation = input("Proceed to payment? (yes/no): ").lower()

    if confirmation == 'yes':
        # Simulate payment processing (in a real app, this is where a payment API would be used)
        print("\nProcessing payment...")

        # Record the order and clear the cart
        import datetime
        order_history.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": user_cart.copy(),
            "total_cost": final_cost
        })
        user_cart = [] # Clear the cart after successful checkout

        print(f"🎉 **Order Placed Successfully!** Your total was ${final_cost:.2f}")
        print("Your food will be delivered soon!")
    else:
        print("↩️ Checkout cancelled. You can continue shopping.")

def show_order_history():
    """Displays all previously placed orders."""
    if not order_history:
        print("\n🗄️ No previous orders found.")
        return

    print("\n--- ⏳ Your Order History ---")
    for i, order in enumerate(order_history):
        print(f"\nOrder #{i+1} placed on: {order['timestamp']}")
        print(f"  Total Cost: **${order['total_cost']:.2f}**")
        print("  Items:")
        for item in order['items']:
            print(f"    - {item['quantity']} x {item['name']}")
    print("-----------------------------")

# --- 3. Main Application Loop ---

def run_application():
    """The main loop for the command-line interface."""
    print("✨ Welcome to the Simple Food Ordering App! ✨")

    while True:
        print("\n--- Main Menu ---")
        print("1. **View Menu**")
        print("2. **Add Item** to Cart")
        print("3. **View Cart** & Calculate Total")
        print("4. **Checkout** & Place Order")
        print("5. **View Order History**")
        print("6. **Exit**")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            display_menu()
            item_id = input("Enter Item ID to add: ")
            quantity = input("Enter Quantity: ")
            add_to_cart(item_id, quantity)
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            show_order_history()
        elif choice == '6':
            print("\n👋 Thank you for using the app! Goodbye.")
            break
        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 6.")

# Start the application
if __name__ == "__main__":
    run_application()
