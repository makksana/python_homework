print('Task 1', end='\n\n')

# Write a function called oops 
# that explicitly raises an IndexError exception when called. 
# Then write another function 
# that calls oops inside a try/except state­ment 
# to catch the error. 
# What happens if you change oops to raise KeyError 
# instead of IndexError?

def oops():
    raise IndexError
    # raise KeyError
    
def error_catch():
    try:
        oops()
    except IndexError:
        print('An IndexError exeption happened')
    except:
        print('Unknown exeption happened')

error_catch()