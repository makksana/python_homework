print('Task 2', end='\n\n')
# Extend Phonebook application

# Functionality of Phonebook application:

# Add new entries 
# Search by first name 
# Search by last name 
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
 

# The first argument to the application 
# should be the name of the phonebook. 
# Application should load JSON data, 
# if it is present in the folder with application, 
# else raise an error. 
# After the user exits, all data should be saved 
# to loaded JSON.
import sys
import json
import pprint

all_contacts = [
    {"name": "Maria",
     "surname": "Onopko",
     "phone": "0987654321",
     "country": "Ukraine",
     "city": "Dnipro"}, 
    {"name": "Dmytro",
     "surname": "Kay",
     "phone": "0980054321",
     "country": "Belarus",
     "city": "Mensk"}, 
    {"name": "Olena",
     "surname": "Zelinska",
     "phone": "098765430",
     "country": "Poland",
     "city": "Warsaw"}, 
    {"name": "Kateryna",
     "surname": "Yershova",
     "phone": "0987600021",
     "country": "Ukraine",
     "city": "Kyiv"}
]


def print_contacts(all_contacts):
    for contact in all_contacts:
        display_one_contact(contact)


def display_one_contact(contact):
    print("{0} {1}, {2}, {3}, {4}".format(contact["name"], contact["surname"], contact["phone"], contact["country"], contact["city"]))


def enter_new_contact():
    new_contact = {}
    new_contact["name"] = input("Enter name: ").title()
    new_contact["surname"] = input("Enter surname: ").title()
    new_contact["phone"] = input("Enter phone: ")
    new_contact["country"] = input("Enter country: ").title()
    new_contact["city"] = input("Enter city: ").title()
    return new_contact


def add_new_contact(all_contacts):
    all_contacts.append(enter_new_contact())


def search_any(all_contacts, q = "", field = "name"):
    result = []
    for contact in all_contacts:
        if contact.get(field) == q:
            result.append(contact)
    return result


def search_by_first_name(all_contacts, first_name):
    res = search_any(all_contacts, first_name, "name")
    if res:
        return res
    print(f"No contact with first name {first_name} found")
    return []


def search_by_last_name(all_contacts, last_name):
    res = search_any(all_contacts, last_name, "surname")
    if res:
        return res
    print(f"No contact with last name {last_name} found")
    return []


def search_by_full_name(all_contacts, full_name):
    parts = full_name.split()
    res = search_by_first_name(all_contacts, parts[0])
    if res and parts[1] != None:
        return search_by_last_name(res, parts[1])
    print(f"No contact with full name {full_name} found")
    return []


def search_by_phone_number(all_contacts, phone_number):
    res = search_any(all_contacts, phone_number, "phone")
    if res:
        return res
    print(f"No contact with phone number {phone_number} found")
    return []
    

def search_by_country(all_contacts, country):
    res = search_any(all_contacts, country, "country")
    if res:
        return res
    print(f"No contact with country {country} found")
    return []


def search_by_city(all_contacts, city):
    res = search_any(all_contacts, city, "city")
    if res:
        return res
    print(f"No contact with city {city} found")
    return []


def get_contact_index_by_phone_number(all_contacts, q = ""):
    for index, contact in enumerate(all_contacts):
        if contact.get("phone") == q:
            return index
    return None


def delete_by_phone_number(all_contacts, phone_number):
    index = get_contact_index_by_phone_number(all_contacts, phone_number)
    if index != None:
        del all_contacts[index]

def update_by_phone_number(all_contacts, phone_number):
    index = get_contact_index_by_phone_number(all_contacts, phone_number)
    if index != None:
        updated_contact = enter_new_contact()
        all_contacts[index] = updated_contact



# with open("phonebook.json", "w") as file_object:
#     json.dump(all_contacts, file_object)


# with open("phonebook.json") as file_object:
#     phonebook = json.load(file_object)
#     pprint.pprint(phonebook)


if __name__ == "__main__":
  # 1. Check if the first argument exists - if not - exit
  # 2. Check if the file named [argument].json exists in current folder - if not - exit with message
  # 3. Output menu and read user input 
  # 
    print_contacts(all_contacts)
#   add_new_contact(all_contacts)
#   print_contacts(all_contacts)
#   first_name = input("Search by first name: ").title()
#   print_contacts(search_by_first_name(all_contacts, first_name))
#   last_name = input("Search by surname: ").title()
#   print_contacts(search_by_last_name(all_contacts, last_name))
#   full_name = input("Search by full name: ").title()
#   print_contacts(search_by_full_name(all_contacts, full_name))
    phone_number = input("Search by number: ")
    # print_contacts(search_by_phone_number(all_contacts, phone_number))
    # print(delete_by_phone_number(all_contacts, phone_number))
    # print_contacts(all_contacts)
    update_by_phone_number(all_contacts, phone_number)
    print_contacts(all_contacts)