#You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

guests_list = ['Rafael', 'Yzach', 'Paul', 'Marc']

name = guests_list[0].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[1].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[2].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[3].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[1].title()
print(f"\nSorry, {name} could not make it to dinner.")

# Yzach could not make it to dinner! Let's invite Yyan instead.
del(guests_list[1])
guests_list.insert(1, 'Yyan')

#Resending Invitations

name = guests_list[0].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[1].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[2].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[3].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

# The dinner table is quite big. I should invite more people to dinner.
print("\nThe dinner table is quite big, Lets invite more people.")
guests_list.insert(0, 'Joshua')
guests_list.insert(2, 'Gab')
guests_list.append('JL')

name = guests_list[0].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[1].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[2].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[3].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[4].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[5].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

name = guests_list[6].title()
print(f"{name}, come to my house and eat dinner at 9pm tonight.")

# The table did not arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests_list.pop()
print(f"Sorry, {name.title()} there's no more room at the table.")

name = guests_list.pop()
print(f"Sorry, {name.title()} there's no more room at the table.")

name = guests_list.pop()
print(f"Sorry, {name.title()} there's no more room at the table.")

name = guests_list.pop()
print(f"Sorry, {name.title()} there's no more room at the table.")

name = guests_list.pop()
print(f"Sorry, {name.title()} there's no more room at the table.")

# There should be two people  in the list. Let's still invite them.
name = guests_list[0].title()
print(f"{name}, please come to dinner theres still 2 seats.")

name = guests_list[1].title()
print(f"{name}, please come to dinner theres still 2 seats.")

del(guests_list[0])
del(guests_list[0])

print(guests_list)