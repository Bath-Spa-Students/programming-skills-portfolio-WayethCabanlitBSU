#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.   
Types_of_sandwiches = ['Teriyaki chicken', 'Meatball', 'Beef onion brisket roast', 'BLT', 'Pastrami sandwich']
#List for finished orders
Finished_sandwich_orders = []
#Add pastrami variable
print("I apologize for the inconvinience but all our pastrami today is out of stock, please order another sandwich")
while 'Pastrami sandwich' in Types_of_sandwiches:
   Types_of_sandwiches.remove('Pastrami sandwich')

while Types_of_sandwiches:
    current_sandwich = Types_of_sandwiches.pop()
    print(f"I'm currently working on your {current_sandwich} sandwich, please wait a moment.")
    Finished_sandwich_orders.append(current_sandwich)

print("\n")
for sandwich in Finished_sandwich_orders:
    print(f"Here is your {sandwich} sandwich.")

