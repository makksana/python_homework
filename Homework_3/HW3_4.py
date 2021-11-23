print('Task 4', end='\n\n')

# Допишите код так, чтобы меняя значение переменной day_of_week 
# выводились следующие сообщения ʼрабочий деньʼ, 'выходной', 'Ошибка! 
# Дни недели считаются 1-7 ни больше ни меньше!'

day_of_week = 5
if day_of_week >= 1 and day_of_week <= 5:
    print('рабочий день')
elif day_of_week == 6 or day_of_week == 7:
    print('выходной')
else:
    print('ошибка')