print('Task 1', end='\n\n')

# A bubble sort can be modified to
# “bubble” in both directions.
# The first pass moves “up” the list and
# the second pass moves “down.”
# This alternating pattern continues
# until no more passes are necessary.
# Implement this variation and
# describe under what circumstances
# it might be appropriate.
import random

def bubble_sort(nums):
    begin = 0
    end = len(nums) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(begin, end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end-1, begin-1, -1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        begin += 1


list_of_nums = [random.randint(1,100) for i in range(10)]
print(list_of_nums)
bubble_sort(list_of_nums)
print(list_of_nums)
