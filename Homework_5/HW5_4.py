print('Task 4', end='\n\n')
# Заполните лист 10ю рандомными значениями в промежутке 1-100. 
# (Испольуя метод randint модуля random) 
# Пока длинна листа меньше 10ти добавляйте к листу элемент.
# Пройдитесь циклом и найдите 
# минимальное и максимальное значение 
# Не используя встроенные методы.

# Выведете минимальное и максимальное значение списка 
# используя встроенные методы.

import random

list = []
len_list = 10
while len_list > 0:
    list.append(random.randint(1, 100))
    len_list-=1
print(list)

minimum = 100
maximum = 1
for number in list:
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number    
print(minimum)
print(maximum)