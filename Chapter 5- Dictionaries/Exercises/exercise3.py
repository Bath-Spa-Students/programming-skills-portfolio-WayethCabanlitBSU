#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

Python_glossary = {
    'Indentation': 'Indentation refers to the spaces at the beginning of a code line',

    'Lists': 'A list is an ordered, and changeable, collection',

    'Elif': 'elif is the same as "else if" in other programming languages',

    'Tuple': 'Used to store multiple items in a single variable.',

    'string': "Is a series of characters stored in a variable",

    'Class variable': "A variable that is shared by all instances of a class.",

    'Objects': "Variables that contain data and functions that can be used to manipulate the data.",

    'Loop': "Is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied.",

    'Comments': "Are identified with a hash symbol, #, and extend to the end of the line",

    'control flow': "The order in which the program's code executes.",
    }


for word, definition in Python_glossary.items():
    print(f"\n{word.title()}: {definition}")