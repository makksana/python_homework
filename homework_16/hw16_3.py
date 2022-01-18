print('Task 3', end='\n\n')

# Create your own implementation of an iterable,
# which could be used inside for-in loop.
# Also, add logic for retrieving elements
# using square brackets syntax.


class Iterator:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            item = self.data[self.index]
            self.index += 1
            return item

    def __getitem__(self, item):
        return self.data[item-1]


word = Iterator("Positive")

for char in word:
    print(char)

print(word.__getitem__(1))
