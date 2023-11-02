Input = "Enter any number to enter the loop: "
while True:
    Loop = input(Input)
    
    Loop= int(Loop)

    if Loop < 10000000000000000:
        print("You are stuck in a loop")