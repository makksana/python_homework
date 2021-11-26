print('Task 1', end='\n\n')
# The greatest number

# Write a Python program to get the largest number 
# from a list of random numbers with the length of 10
# Constraints: 
# use only while loop and random module to generate numbers


import random

list = []
len_list = 10
while len_list > 0:
    len_list -= 1
    list.append(random.randint(0, 100))
    
print(list)
print('The largest number from a list', max(list))
