print('Task 7', end='\n\n')
# Реверс.

# Создайте лист длинной 10 с подряд идущими значениями. 
# Используя цикл переверните лист. 
# (для этого надо поменять первый с последним, 
# второй с предпоследним и так далее)

list = []
len_list = 0
while len_list < 10:
    len_list+=1
    list.append(len_list)

print(list)

# result_list =list[::-1]

reversed_list = []
while len(list) > 0:
    reversed_list.append(list.pop())

print(reversed_list)