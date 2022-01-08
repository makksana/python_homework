print('Task 1', end='\n\n')

# Write a decorator that prints a function 
# with arguments passed to it.

# NOTE! It should print the function, 
# not the result of its execution!

# For example:
#  "add called with 4, 5"

from functools import wraps
 

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__ + ' called with ' + ', '.join(str(x) for x in (args, kwargs)))
    return wrapper


@logger
def add(x, y):
    return x + y

add(4,5) 


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

square_all(2,3,a=4)