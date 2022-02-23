from typing import List
from min_bin_heap import BinHeap
print('Task 2', end='\n\n')

# Using the BinaryHeap class,
# implement a new class called PriorityQueue.
# Your PriorityQueue class should implement the constructor,
# plus the enqueue and dequeue methods.


class PriorityQueue:
    def __init__(self, items: List[int] = []) -> None:
        self._items = BinHeap()
        if items != []:
            self._items.build_heap(items)

    def enqueue(self, item):
        self._items.insert(item)

    def dequeue(self):
        return self._items.del_min()


if __name__ == "__main__":
    q = PriorityQueue([5, 3, 17, 10, 84, 19, 6, 22, 9])
    q.enqueue(11)
    q.enqueue(77)
    print(q.dequeue())  # 3
    print(q.dequeue())  # 5
