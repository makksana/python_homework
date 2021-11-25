print('Task 3', end='\n\n')
# Words combination

# Create a program that reads an input string and 
# then creates and prints 5 random strings 
# from characters of the input string.
# For example, the program obtained the word ‘hello’, 
# so it should print 5 random strings(words) 
# that combine characters 
# ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)
import random

your_word = input('Enter your word: ')

number_of_strings = 5
while number_of_strings > 0:
    number_of_strings -= 1
    new_word = your_word
    word = ''
    while len(word) < len(your_word):
        index = random.randint(0, len(new_word)-1)
        word += new_word[index] 
        new_word = new_word[:index]+new_word[index+1:] 
    print(word)
      


    # one_letter = random.choice(your_word)
    # # len(your_word)
    # print(one_letter)

    # mylist = [[0], [1], "cherry"]
    # random.shuffle(mylist)



# while number_of_strings >= 5:
#    number_of_strings+=1
#     new_word = random.choice(your_word)
#     print(new_word)
