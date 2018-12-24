import os

shopping_cart = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to show this help.
Enter 'SHOW' to view shopping cart.
""")
    
    
def add_to_list(item):
    shopping_cart.append(item)
    if len(shopping_cart) == 1:
        print(f"Item added! There is currently {len(shopping_cart)} item in your cart")
    else:
        print(f"Item added! There are currently {len(shopping_cart)} items in your cart")


def show_list():
    print("Here's your list:")
    for item in shopping_cart.copy():
        print("* " + item)
        
        
show_help()

while True:
    new_item = input("> ")    
    if new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        show_list()
        continue
    elif new_item == 'HELP':
        show_help()
        continue
    else:
        add_to_list(new_item)
        
        
show_list()