from typing import Optional
print('Task 1', end='\n\n')
# Task should be solved using recursion


def to_power(x: Optional[float], exp: int) -> Optional[float]:
    """
    Returns  x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    ValueError: This function works only with exp > 0.
    """

    if exp < 0:
        raise ValueError('This function works only with exp > 0')
    if x == 0 or x == 1:
        return x
    if exp == 0:
        return 1
    rez = x*to_power(x, exp-1)
    return rez


assert (to_power(2, 3) == 8) == True
assert (to_power(3.5, 2) == 12.25) == True
