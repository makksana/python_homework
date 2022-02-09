from read_books import read_books_per_month
print('Task 1', end='\n\n')
# Imports practice

# Make a directory with 2 modules
# make a function in one of them
# then import this function in the other module
# and use that in your script of choice.

read_books_per_year = int(
    input('How many books do you want to read this year? '))


per_month = read_books_per_month(read_books_per_year)


print(f'You should read {int(per_month)} books per month to obtain your goal')
