#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
Python_glossary = {
    'Indentation': 'Indentation refers to the spaces at the beginning of a code line',
    'Lists': 'A list is an ordered, and changeable, collection',
    'Elif': 'elif is the same as "else if" in other programming languages',
    'Tuple': 'Used to store multiple items in a single variable.',
    'string': "Is a series of characters stored in a variable",
    }

Terminologies = 'Indentation'
print(f"\n{Terminologies.title()}: {Python_glossary[Terminologies]}")

Terminologies = 'Lists'
print(f"\n{Terminologies.title()}: {Python_glossary[Terminologies]}")

Terminologies = 'Elif'
print(f"\n{Terminologies.title()}: {Python_glossary[Terminologies]}")

Terminologies = 'Tuple'
print(f"\n{Terminologies.title()}: {Python_glossary[Terminologies]}")

Terminologies = 'string'
print(f"\n{Terminologies.title()}: {Python_glossary[Terminologies]}")