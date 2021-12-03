print('Task 2', end='\n\n')

# Write a function that takes in two numbers 
# from the user via input(), 
# call the numbers a and b, 
# and then returns the value of squared a divided by b, 
# construct a try-except block 
# which raises an exception 
# if the two values given 
# by the input function were not numbers, 
# and if value b was zero (cannot divide by zero).  
    
def numbers():
    try:
        a = input('Enter first number:')
        b = input('Enter second number:')
        return int(a)**2/int(b)
    except ValueError:
        print('It is not numbers')
    except ZeroDivisionError:
        print('Cannot divide by zero')
result = numbers()
if result != None:
    print(result)