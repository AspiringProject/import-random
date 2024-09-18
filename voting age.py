# Simple Python program with errors

# Set the price of an item
item_price = 19.99

# Get the amount of money the user has
user_money = int(input("Enter the amount of money you have: "))

# Check if the user can afford the item
if user_money >= item_price:
    print("You can buy the item!")
else:
    print("Sorry, you don't have enough money to buy the item.")
