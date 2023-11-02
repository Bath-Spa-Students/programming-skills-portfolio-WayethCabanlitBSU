#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.

Input_topping = "\n What kind of toppings would you like for your pizza?"
Input_topping  += "\n If you are done inputting toppings Enter 'quit': "

while True:
    topping = input(Input_topping)
    if topping != 'quit':
        print(f" Thank you for your input I will add {topping} to your pizza.")
        print(f" Would you like anything else?")
    else:
        break
   