print('Task 2', end='\n\n')

# Write a Python program 
# to access a function inside a function 
# (Tips: 
# use function, which returns another function)

def make_expration(x):
    def calculate_expression(y):
        return x**2+2*x+y
    return calculate_expression

print(make_expration(5)(2))