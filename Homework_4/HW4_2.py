print('Task 2', end='\n\n')
# The birthday greeting program.

# Write a program that takes your name as input, 
# and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

name = input('What is your name? ')
while True:
    age = input('How old are you? ')
    if age.isdigit():
        age = int(age)+1
        print('Hello %s, on your next birthday you’ll be %i years'%(name.capitalize(), age))
        break