print('Task 4', end='\n\n')
# Task should be solved using recursion


def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """
    if len(input_str) == 0:
        return input_str
    return reverse(input_str[1:]) + input_str[0]


assert reverse("hello") == "olleh"
assert reverse("o") == "o"
assert reverse("Typography") == "yhpargopyT"
