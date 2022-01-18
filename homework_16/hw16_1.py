print('Task 1', end='\n\n')

# Create your own implementation of
# a built-in function enumerate,
# named `with_index`,
# which takes two parameters:
# `iterable` and `start`, default is 0.
#
# Tips: see the documentation for the enumerate function


def with_index(iterable, start=0):
    n = start
    for item in iterable:
        yield n, item
        n += 1


print(list(with_index('Typography')))
print(dict(with_index('Typography')))
print(tuple(with_index('Typography')))
print(set(with_index('Typography')))