from typing import Optional
print('Task 3', end='\n\n')
# Task should be solved using recursion


def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    ValueError("This function works only with postive integers")
    """
    if a < 0 or n < 0:
        raise ValueError("This function works only with postive integers")
    if a == 0 or n == 0:
        return 0
    if n == 1:
        return a
    return a + mult(a, n-1)


assert (mult(2, 4) == 8) == True
assert (mult(2, 0) == 0) == True
