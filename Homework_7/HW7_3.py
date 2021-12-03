print('Task 3', end='\n\n')
# A simple calculator.

# Create a function called make_operation, 
# which takes in a simple arithmetic operator 
# as a first parameter 
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
# and an arbitrary number of arguments (only numbers) 
# as the second parameter. 
# Then return the sum or product of all the numbers 
# in the arbitrary parameter. 
# For example:

# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42  

def make_operation(operator, *args):
    total = args[0]
    for item in args[1:]:
        if operator == '+':
            total += item
        elif operator == '-':
            total -= item
        elif operator == '*':
            total *= item
        else:
            print('Invalid operator!') 
            return

    print(total)

make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20) 
make_operation('*', 7, 6)
make_operation('/', 15, 5)