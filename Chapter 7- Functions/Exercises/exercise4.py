#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
def make_shirt(shirt_size='large', shirt_design='CC gang, I love python!'):
   
   print(f"\nMy shirt should a {shirt_size} t-shirt so it would fit me.")
   print(f'The design on my shirt will be, "{shirt_design}"')

make_shirt()
make_shirt(shirt_size='medium')
make_shirt('small', 'Programming is not suffering')