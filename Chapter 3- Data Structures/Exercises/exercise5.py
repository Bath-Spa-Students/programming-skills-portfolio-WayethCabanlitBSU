#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.

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