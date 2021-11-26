print('Task 2', end='\n\n')
# Exclusive common numbers.

# Generate 2 lists with the length of 10 
# with random integers from 1 to 10, 
# and make a third list containing the common integers 
# between the 2 initial lists without any duplicates.
# Constraints: 
# use only while loop and random module to generate numbers


import random

list_1 = []
list_2 = []
len_list = 10
while len_list > 0:
    list_1.append(random.randint(0, 10))
    list_2.append(random.randint(0, 10))
    len_list -= 1
print(list_1)
print(list_2)

common_list = list(set(list_1+list_2))
print(common_list)