class ShoppingCart:
    def __init__(self):
        # Initializes an empty shopping cart
        self.cart = {}

    def add_item(self, name, price, quantity=1):
        """Adds an item to the shopping cart."""
        if name in self.cart:
            self.cart[name]['quantity'] += quantity
        else:
            self.cart[name] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} of {name} to the cart.")

    def remove_item(self, name, quantity=None):
        """Removes an item or reduces its quantity in the shopping cart."""
        if name in self.cart:
            if quantity is None or quantity >= self.cart[name]['quantity']:
                del self.cart[name]
                print(f"Removed {name} from the cart.")
            else:
                self.cart[name]['quantity'] -= quantity
                print(f"Removed {quantity} of {name} from the cart.")
        else:
            print(f"{name} is not in the cart.")

    def view_cart(self):
        """Displays all items in the shopping cart with a total price."""
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your shopping cart contains:")
            total = 0
            for item, details in self.cart.items():
                item_total = details['price'] * details['quantity']
                total += item_total
                print(f"{item} - ${details['price']} x {details['quantity']} = ${item_total}")
            print(f"Total: ${total}")

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.cart.clear()
        print("Your cart is now empty.")

# Example Usage

