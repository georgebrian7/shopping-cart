from main import ShoppingCart

cart = ShoppingCart()
cart.add_item("Apple", 12, 4)
cart.add_item("Banana", 8, 6)
cart.add_item("rice",20,2)
cart.add_item("biscuit",5,2)
cart.add_item("kales",9,4)
cart.add_item("book",30,5)

print(cart.remove_item("Apple",2))
print(cart.view_cart())
