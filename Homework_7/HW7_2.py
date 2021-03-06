print('Task 2', end='\n\n')
# Creating a dictionary.

# Create a function called make_country, 
# which takes in a country’s name 
# and capital as parameters. 
# Then create a dictionary from those two, 
# with ‘name’ as a key and ‘capital’ 
# as a parameter. 
# Make the function print out 
# the values of the dictionary to make sure 
# that it works as intended.

def make_country(country_name, capital):
    countries = {country_name: capital}
    print(countries.get(country_name))

make_country('Ukraine', 'Kyev')
make_country('USA', 'Washington')
make_country('England', 'London')
