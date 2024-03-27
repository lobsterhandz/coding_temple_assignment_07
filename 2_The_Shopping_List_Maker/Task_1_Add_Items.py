# Initialize an empty shopping list
shopping_list = []

# Function to add an item to the shopping list
def add_item_to_list():
    print("\nAvailable items to add: apple, orange, pears")
    item = input("Which item would you like to add (or type 'done' to finish)? ")
    return item

# Loop to continuously ask for items to add
while True:
    user_input = add_item_to_list()
    
    # Check if the user wants to finish adding items
    if user_input.lower() == 'done':
        break
    elif user_input in ['apple', 'orange', 'pears']:
        shopping_list.append(user_input)
        print(f"{user_input} has been added to your shopping list.")
    else:
        print("Sorry, you can only add apple, orange, or pears. Type 'done' to finish.")
        
# Print the final shopping list
print("\nYour shopping list:")
for item in shopping_list:
    print(f"- {item}")
