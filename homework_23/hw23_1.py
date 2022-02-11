import pprint
import json
import sys
from typing import Optional
print('Task 1', end='\n\n')
# Practise type annotations

# Go to your implementation of the Phonebook application
# from module 1 or any other comprehensive code,
# which you have done during the course,
# and annotate this code with type hints,
# using knowledge from this lesson.


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


def print_contacts(all_contacts: list[dict]) -> None:
    for contact in all_contacts:
        display_one_contact(contact)


def display_one_contact(contact: dict[str]) -> None:
    print("{0} {1}, {2}, {3}, {4}".format(
        contact["name"], contact["surname"], contact["phone"], contact["country"], contact["city"]))


def enter_new_contact() -> dict[str]:
    new_contact = {}
    new_contact["name"] = input("Enter name: ").title()
    new_contact["surname"] = input("Enter surname: ").title()
    new_contact["phone"] = input("Enter phone: ")
    new_contact["country"] = input("Enter country: ").title()
    new_contact["city"] = input("Enter city: ").title()
    return new_contact


def add_new_contact(all_contacts: list[dict]) -> None:
    all_contacts.append(enter_new_contact())


def search_any(all_contacts: list[dict], q: str = "", field: str = "name") -> list[dict]:
    result = []
    for contact in all_contacts:
        if contact.get(field) == q:
            result.append(contact)
    return result


def search_by_first_name(all_contacts: list[dict], first_name) -> Optional[list]:
    res: list = search_any(all_contacts, first_name, "name")
    if res:
        return res
    print(f"No contact with first name {first_name} found")
    return []


def search_by_last_name(all_contacts: list[dict], last_name: str) -> Optional[list]:
    res: list = search_any(all_contacts, last_name, "surname")
    if res:
        return res
    print(f"No contact with last name {last_name} found")
    return []


def search_by_full_name(all_contacts: list[dict], full_name: str) -> Optional[list]:
    parts: str = full_name.split()
    res: list = search_by_first_name(all_contacts, parts[0])
    if res and parts[1] != None:
        return search_by_last_name(res, parts[1])
    print(f"No contact with full name {full_name} found")
    return []


def search_by_phone_number(all_contacts: list, phone_number: str) -> Optional[list]:
    res: list = search_any(all_contacts, phone_number, "phone")
    if res:
        return res
    print(f"No contact with phone number {phone_number} found")
    return []


def search_by_country(all_contacts: list, country: str) -> Optional[list]:
    res: list = search_any(all_contacts, country, "country")
    if res:
        return res
    print(f"No contact with country {country} found")
    return []


def search_by_city(all_contacts: list, city: str) -> Optional[list]:
    res: list = search_any(all_contacts, city, "city")
    if res:
        return res
    print(f"No contact with city {city} found")
    return []


def get_contact_index_by_phone_number(all_contacts: dict, q: str = "") -> None:
    for index, contact in enumerate(all_contacts):
        if contact.get("phone") == q:
            return index
    return None


def delete_by_phone_number(all_contacts: dict, phone_number: str) -> None:
    index: int = get_contact_index_by_phone_number(all_contacts, phone_number)
    if index != None:
        del all_contacts[index]


def update_by_phone_number(all_contacts: dict, phone_number: str) -> None:
    index: int = get_contact_index_by_phone_number(all_contacts, phone_number)
    if index != None:
        updated_contact: dict = enter_new_contact()
        all_contacts[index] = updated_contact


if __name__ == "__main__":

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
