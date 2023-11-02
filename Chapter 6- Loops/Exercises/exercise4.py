#Make a list called sandwich_orders and fill it with the names of various sandwiches.
Types_of_sandwiches = ['Teriyaki chicken', 'Meatball', 'Beef onion brisket roast', 'BLT']
#List for finished orders
Finished_sandwich_orders = []

while Types_of_sandwiches:
    current_sandwich = Types_of_sandwiches.pop()
    print(f"I'm currently working on your {current_sandwich} sandwich, please wait a moment.")
    Finished_sandwich_orders.append(current_sandwich)

print("\n")
for sandwich in Finished_sandwich_orders:
    print(f"Here is your {sandwich} sandwich.")

