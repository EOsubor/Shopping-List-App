import os

shopping_cart = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    clear_screen()
    print("What should we pick up at the store today?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to show this help.
Enter 'SHOW' to view shopping cart.
""")

def show_list():
    clear_screen()
    print("Here's your list:")
    for index, item in enumerate(shopping_cart, 1):
        print(f"{index}. {item}")
    print("_" * 10)

def remove_from_cart():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_cart.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

def add_to_list(item):
    show_list()
    if shopping_cart:
        position = input(f"Where should I add {item}\n"
                         "Press 'ENTER' to add to the end of the list\n"
                         "> ")
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_cart.insert(position-1, item)
    else:
        shopping_cart.append(item)

    show_list()

show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_cart()
    else:
        add_to_list(new_item)


show_list()
