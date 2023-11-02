#Make a dictionary containing three major rivers and the country each river runs through. 
Famous_Rivers = {
    'Amazon River': 'South America',
    'Ganges river': 'India',
    'Kenai River': 'Alaska',
    'Caño Cristales': 'Colombia',
    'The Colorado River': 'US State of Colorado',
    }

for river, country in Famous_Rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in Famous_Rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in Famous_Rivers.values():
    print(f"- {country.title()}")