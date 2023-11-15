#Loop code using list
Start_loop = ["Loop"]

while Start_loop:
    current_loop = Start_loop.pop()
    print(f"You are stuck in a {current_loop}, please wait a moment.")
    Start_loop.append(current_loop)

#Input loop
Input = "Enter any number to enter the loop: "
while True:
    Loop = input(Input)
    
    Loop= int(Loop)

    if Loop < 10000000000000000:
        print("You are stuck in a loop")

