print('Task 2', end='\n\n')

# Write a program that reads in
# a sequence of characters,
# and determines whether it's
# parentheses, braces, and curly brackets
# are "balanced."


class Stack():
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return (self._stack == [])


def is_balanced(braces_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(braces_string) and balanced:
        symbol = braces_string[index]

        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.is_empty():
        return True
    return False


def matches(open, close):
    braces = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    return braces.get(open) == close


print(is_balanced('{({([][])}())}'))
print(is_balanced('[{()]'))
print(is_balanced('}()]'))
