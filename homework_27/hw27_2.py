print('Task 2', end='\n\n')

# Implement a stack using a singly linked list.


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class StackAsUnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def push(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def pop(self):
        if self._head is None:
            raise ValueError('Stack is empty')
        popped = self._head.get_data()
        self._head = self._head.get_next()
        return popped

    def peek(self):
        if self._head is None:
            raise ValueError('Stack is empty')
        peeked = self._head.get_data()
        return peeked

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def __repr__(self):
        representation = "<StackAsUnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


s = StackAsUnorderedList()
print(s)
s.push(39)
print(s)
s.push(2)
print(s)
s.push(155)
print(s)
s.push(43)
print(s)
s.push(7)
print(s)
print(s.pop())
print(s)
print(s.peek())
print(s)
