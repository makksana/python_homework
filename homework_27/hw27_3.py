print('Task 3', end='\n\n')

# Implement a queue using a singly linked list.


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


class QueueAsUnorderedList:

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():
            self._head = temp
        else:
            self._tail.set_next(temp)
        self._tail = temp

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        temp = self._head.get_data()
        next_node = self._head.get_next()
        if not next_node:
            self._tail = next_node
        self._head = next_node
        return temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def __repr__(self):
        representation = "<QueueAsUnorderedList: Head -> "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + " <- Tail>"

    def __str__(self):
        return self.__repr__()


q = QueueAsUnorderedList()
print(q)
q.enqueue(45)
print(q)
q.enqueue(1)
print(q)
q.enqueue(7800)
print(q)
q.enqueue(243)
print(q)
q.enqueue(9)
print(q)
print(q.dequeue())
print(q)
q.enqueue(82)
print(q)
