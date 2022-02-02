print('Task 3', end='\n\n')

# Extend the Stack to include
# a method called get_from_stack
# that searches and returns an element e from a stack.
# Any other element must remain on the stack
# respecting their order.
# Consider the case in which the element is not found -
# raise ValueError with proper info Message


# Extend the Queue to include
# a method called get_from_stack
# that searches and returns an element e from a queue.
# Any other element must remain in the queue
# respecting their order.
# Consider the case in which the element is not found -
# raise ValueError with proper info Message


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return (self.stack == [])

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self.stack), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_stack(self, e) -> bool:
        new_stack = []

        while not self.is_empty():
            new_item = self.pop()
            new_stack.append(new_item)

        found = False
        while new_stack:
            item = new_stack.pop()
            if e == item and not found:
                found = True
                continue
            self.push(item)
        return found


s = Stack()
word = 'Typography'
for char in word:
    s.push(char)

print(s)
print(s.get_from_stack('p'))
print(s)


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return (self._items == [])

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_stack(self, e) -> bool:
        new_queue = []

        while not self.is_empty():
            new_item = self.dequeue()
            new_queue.insert(0, new_item)

        found = False
        while new_queue:
            item = new_queue.pop()
            if e == item and not found:
                found = True
                continue
            self.enqueue(item)
        return found


q = Queue()
word = 'Typography'
for char in word:
    q.enqueue(char)

print(q)
print(q.get_from_stack('p'))
print(q)
