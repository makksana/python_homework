print('Task 3', end='\n\n')
# Extracting numbers.

# Make a list that contains all integers from 1 to 100, 
# then find all integers from the list 
# that are divisible by 7 
# but not a multiple of 5, 
# and store them in a separate list. 
# Finally, print the list.
# Constraint: 
# use only while loop for iteration


list = []
len_list = 0
while len_list < 100:
    len_list+=1
    list.append(len_list)

result_list =[]
for number in list:
    if number%7==0 and number%5!=0:
        result_list.append(number)

print(result_list)