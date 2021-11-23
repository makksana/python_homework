print('Task 1', end='\n\n')
# String manipulation

# Write a Python program to get a string made of the first 2 and 
# the last 2 chars from a given string. 
# If the string length is less than 2, return instead of the empty string.

# Sample String: 'helloworld'
# Expected Result : 'held'
# Sample String: 'my'
# Expected Result : 'mymy'
# Sample String: ' x'
# Expected Result: Empty String

sample_string = input('Write down one word: ')
if len(sample_string)>=2:
    expected_result = sample_string[0:2]+sample_string[-2]+sample_string[-1]
    print(f'{expected_result}')
else:
    print('Empty string')

# Tips:
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and 
# negative indexing to get the last characters