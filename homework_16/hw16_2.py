print('Task 2', end='\n\n')

# Create your own implementation of
# a built-in function range,
# named in_range(),
# which takes three parameters:
# `start`, `end`, and optional step.
#
# Tips: See the documentation for `range` function


def in_range(start, end, step=1):
    while start <= end:
        yield start
        start += step


print(list(in_range(-10, 10, 3)))
