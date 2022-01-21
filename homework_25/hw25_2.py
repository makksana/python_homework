from typing import Optional
print('Task 2', end='\n\n')
# Task should be solved using recursion


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    """

    if len(looking_str) < 1:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    else:
        return is_palindrome(looking_str[1:-1])


assert is_palindrome('mom') == True
assert is_palindrome('sassas') == True
assert is_palindrome('o') == True
assert is_palindrome('santa') == False
