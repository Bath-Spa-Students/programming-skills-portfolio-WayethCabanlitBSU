#Updated loop made using list
Start_loop = ["Loop"]

while Start_loop:
    current_loop = Start_loop.pop()
    print(f"You are stuck in a {current_loop}, please wait a moment.")
    Start_loop.append(current_loop)

