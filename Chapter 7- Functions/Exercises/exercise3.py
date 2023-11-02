#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
def make_shirt(shirt_size, shirt_design):
    print(f"\nMy shirt should a {shirt_size} t-shirt so it would fit me.")
    print(f'The design on my shirt will be, "{shirt_design}"')

make_shirt('Medium', 'Bathspa logo with the message CC YEAR 1 STUDENT')
#Make another shirt but with a different size   
make_shirt(shirt_design="A picture of a cat using the computer", shirt_size='Large')