#Make several dictionaries, where the name of each dictionary is the name of a pet. 
pets = []

pet = {
    'Type of animal': 'Persian cat',
    'pet name': 'Lilac',
    'owner of pet': 'Rafael',
    'weight': 5,
    'eats': 'Cat food and treats',
}
pets.append(pet)

pet = {
    'Type of animal': 'Samoyed dog',
    'pet name': 'Cloud',
    'owner of pet': 'Reign',
    'weight': 13,
    'eats': 'Meat and dog food',
}
pets.append(pet)

pet = {
    'Type of animal': 'Raccoon',
    'pet name': 'Rigby',
    'owner of pet': 'Mordecai',
    'weight': 9,
    'eats': 'Trash',
}
pets.append(pet)

# Displays information about each pet and owner.
for pet in pets:
    print(f"\n I have information about each of their pet {pet['pet name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")