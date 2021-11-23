print('Task 2', end='\n\n')
# The valid phone number program

# Make a program that checks 
# if a string is in the right format for a phone number. 
# The program should check that the string contains only numerical characters 
# and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string evaluation.

phone_number = input('Enter your phone number, only 10 digits: ')
if len(phone_number)==10 and phone_number.isnumeric():
    print(f'{phone_number} is a valid phone number')
else:
    print(f'{phone_number} is not a phone number')