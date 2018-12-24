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
    index = 1
    for item in shopping_cart:                 
        print(f"{index}. {item}")
        index += 1    
    print("_" * 10)
    
    
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
        shopping_cart.append(new_item)                 
    
    show_list() 
              
show_help()

while True:
    new_item = input("> ")  
    
    if new_item.upper() == 'DONE' or new_item == 'QUIT':
        break
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    else:
        add_to_list(new_item)
        
        
show_list()