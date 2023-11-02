#Write a function called describe_city() that accepts the name of a city and its country. 
def city_country(capital_city, country):
    return f"{capital_city.title()}, {country.title()}"

capital_city = city_country('Moscow', 'Russia')
print(capital_city)

capital_city = city_country('Beijing', 'China')
print(capital_city)

capital_city = city_country('Pyongyang', 'North Korea')
print(capital_city)

