print('Task 1', end='\n\n')

# Implement binary search using recursion.


def binary_search(iter, item):
    if len(iter) == 0:
        return False

    midpoint = len(iter)//2
    if iter[midpoint] == item:
        return True

    if item < iter[midpoint]:
        return binary_search(iter[:midpoint], item)

    return binary_search(iter[midpoint+1:], item)


new_iter = [1, 4, 13, 19, 32, 42, 67, 105]
print(binary_search(new_iter, 17))
print(binary_search(new_iter, 42))
