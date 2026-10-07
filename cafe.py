menu={
    "tea":20,
    "coffee":100,
    "juice":50}
print(menu)

def get_menu(name, order, quantity):
    name=input("what is your name?:")
    order=input("what would you like to order?: ")
    quantity=input("how many?: ")
    return name, order, quantity


while True:
    name, order, quantity = get_menu("Alice", "tea", 2)
    if order in menu:
        total = menu[order] * int(quantity)
        print(f"{name}, your total for {quantity} {order}(s) is: {total}")
    elif order == "exit":
        print("Thank you for visiting. Goodbye!")
        break
    else:
        print(f"Sorry {name}, we don't have {order} on the menu.")


8










