print('Task 2', end='\n\n')

# Read about the Fibonacci search and
# implement it using python.
# Explore its complexity and
# compare it to sequential,
# binary searches.


# O (log n); the algorithm is faster than
# both linear search and jump search in most cases.
# Fibonacci search can be used when
# we have a very large number of elements
# to search through,
# and we want to reduce the
# inefficiency associated with using an algorithm
# which relies on the division operator.
# An additional advantage of using Fibonacci search is
# that it can accommodate input arrays
# that are too large to be held in CPU cache or RAM,
# because it searches through elements in increasing step sizes,
# and not in a fixed size.
def fibonacci_search(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1
    return -1


print(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 6))
