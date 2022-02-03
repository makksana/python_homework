from xml.dom import NotFoundErr


print('Task 1', end='\n\n')
# Extend UnorderedList

# Implement append, index, pop,
# insert methods for UnorderedList.
# Also implement a slice method,
# which will take two parameters `start` and `stop`,
# and return a copy of the list starting at the position
# and going up to but not including the stop position.


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


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous is None:
                self._head = current.get_next()
            else:
                previous.set_next(current.get_next())
        else:
            raise NotFoundErr(f'{item} is not in list')

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()

    def append(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            return
        last = self._head

        while last.get_next():
            last = last.get_next()
        last.set_next(new_node)

    def index(self, item):
        current = self._head
        found = False
        index = 0
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index += 1

        return index if found else None

    def pop(self):
        if self._head is None:
            return None
        current = self._head
        previous = None

        while current.get_next():
            previous = current
            current = current.get_next()
        if previous:
            previous.set_next(None)
        else:
            self._head = None

    def insert(self, index, item):
        if index > self.size():
            raise IndexError
        current = self._head
        previous = None
        while index > 0:
            index -= 1
            previous = current
            current = current.get_next()
        new_node = Node(item)
        new_node.set_next(current)
        if previous:
            previous.set_next(new_node)
        else:
            self._head = new_node

    def slice(self, start, stop):
        if start < 0 or stop <= start or stop > self.size():
            raise IndexError()
        sliced = UnorderedList()
        stop -= start

        current = self._head
        while start > 0:
            current = current.get_next()
            start -= 1
        while stop > 0:
            sliced.append(current.get_data())
            current = current.get_next()
            stop -= 1
        return sliced


my_list = UnorderedList()
print(my_list)
my_list.insert(0, 10)
print(my_list)
print('slice(0,1)', my_list.slice(0, 1))
my_list.insert(0, 20)
print(my_list)
my_list.insert(2, 30)
print(my_list)
my_list.insert(0, 40)
my_list.insert(0, 50)
my_list.insert(0, 60)
my_list.insert(0, 70)
my_list.insert(0, 80)
my_list.insert(0, 90)
print(my_list)
print('slice(2,5)', my_list.slice(2, 5))
my_list.append(31)
print(my_list)
my_list.append(77)
print(my_list)
print(my_list.index(35))
print(my_list.index(77))
print(my_list.index(31))
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)
my_list.pop()
print(my_list)
