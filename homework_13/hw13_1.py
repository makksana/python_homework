print('Task 1', end='\n\n')

# Write a Python program to detect 
# the number of local variables 
# declared in a function.


def collection_of_var():
    var1, var2, var3, var4 = 12, 87, True, 15
    var5 = 'Hello, there'
    var6 = '3'
    var7, var8, var9 = None, 347, False
  
print(collection_of_var.__code__.co_nlocals)