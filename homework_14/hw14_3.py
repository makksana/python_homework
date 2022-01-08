print('Task 3', end='\n\n')

# Write a decorator `arg_rules` 
# that validates arguments passed to the function.

# A decorator should take 3 arguments:

# max_length: 15

# type_: str

# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, 
# the function should return False 
# and print the reason it failed; 
# otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name):
            changed = func(name)
            if type(name)!=type_:
                print('You put name with wrong type')
                return False
            if len(name) > max_length:
                print('Length of name should be less than 15 characters')
                return False
            for contain in contains:
                if name.find(contain) == -1:
                    print(f'Name should contain {contains}')
                    return False
            return changed
        return wrapper
    return decorator

 
@arg_rules(type_=str, max_length=15, contains=['05', '@'])

def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

 
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'