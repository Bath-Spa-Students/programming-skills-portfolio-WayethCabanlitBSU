#A movie theater charges different ticket prices depending on a person’s age. 
#Input age 

Input_age = "What is your age?"
Input_age += "\nEnter 'quit' when you are finished entering your age: "

while True:
    age = input(Input_age )
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  For children 3 and below you get the ticket for free!")
    elif age < 13:
        print("  For ages 4-13 your ticket price is 10$")
    else:
        print("  For ages 13 and above your ticket price is 15$")

 