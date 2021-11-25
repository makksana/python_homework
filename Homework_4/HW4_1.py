print('Task 1', end='\n\n')
# The Guessing Game.

# Write a program that generates a random number 
# between 1 and 10 and 
# lets the user guess what number was generated. 
# The result should be sent back to the user via a print statement.

import random

print("Let`s play The Guessing Game")
player = input('Choose number from 1 to 10: ')
computer = str(random.randint(1, 10))
if (computer == player):
    print('You won!')
else:
    print(f'You loose, the number was {computer}:(')
