# Initialize an empty shopping list
shopping_list = []

# Function to show the current shopping list
def show_shopping_list():
    print("\nYour current shopping list:")
    for item in shopping_list:
        print(f"- {item}")
    if not shopping_list:
        print("It's empty!")

# Function to add an item to the shopping list
def add_item_to_list():
    print("\nAvailable items to add: apple, orange, pears")
    item = input("Which item would you like to add (or type 'done' to finish, 'remove' to delete an item)? ")
    return item

# Function to remove an item from the shopping list
def remove_item_from_list():
    show_shopping_list()
    item = input("Which item would you like to remove? ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in the shopping list, so it can't be removed.")

# Main loop to add or remove items
while True:
    user_input = add_item_to_list()
    
    if user_input.lower() == 'done':
        break
    elif user_input.lower() == 'remove':
        remove_item_from_list()
    elif user_input in ['apple', 'orange', 'pears']:
        shopping_list.append(user_input)
        print(f"{user_input} has been added to your shopping list.")
    else:
        print("Sorry, you can only add apple, orange, or pears. Type 'done' to finish or 'remove' to delete an item.")

# Showing the final shopping list
show_shopping_list()
