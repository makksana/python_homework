print('Task 4', end='\n\n')
# The math quiz program

# Write a program that asks the answer 
# for a mathematical expression, 
# checks whether the user is right or wrong, 
# and then responds with a message accordingly.

question = int(input('What an answer is for (2*5+8)/3? '))
answer = (2*5+8)/3
if answer == question:
    print('You are wright! The answer is %d'%(answer))
else:
    print('You are wrong! The answer is %d'%(answer))   