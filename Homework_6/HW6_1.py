print('Task 1', end='\n\n')

# Make a program that has some sentence (a string) on input 
# and returns a dict containing all unique words 
# as keys and the number of occurrences as values. 

sentence = input('Enter sentence: ').lower().strip().split(' ')

list_of_words = [word.strip('!,.:;?*/|[{]}-_–+=#') for word in sentence]
unique_words = {item:list_of_words.count(item) for item in list_of_words}

print(unique_words)