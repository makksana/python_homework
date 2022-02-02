print('Task 1', end='\n\n')

# Write a program that reads in
# a sequence of characters and
# prints them in reverse order,
# using your implementation of Stack.


class Stack():
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return (self._stack == [])


def reverse(sequence):
    stack = Stack()
    reversed = ''

    for char in sequence:
        stack.push(char)

    while not stack.is_empty():
        reversed += stack.pop()
    return reversed


print(reverse('Typography'))
