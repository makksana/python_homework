import random
print('Task 2', end='\n\n')

# Implement the mergeSort function
# without using the slice operator.


def mergeSort(alist):
    width = 1
    n = len(alist)
    while (width < n):
        left = 0
        while (left < n):
            right = min(left+(width*2-1), n-1)
            mid = (left+right)//2
            if (width > n//2):
                mid = right-(n % width)
            merge(alist, left, mid, right)
            left += width*2
        width *= 2
    return alist


def merge(alist, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = alist[left + i]
    for i in range(0, n2):
        R[i] = alist[mid + i + 1]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i] > R[j]:
            alist[k] = R[j]
            j += 1
        else:
            alist[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        alist[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        alist[k] = R[j]
        j += 1
        k += 1


alist = [random.randint(1, 100) for i in range(10)]
print("Unsorted list is ")
print(alist)

mergeSort(alist)

print("Sorted list is ")
print(alist)
