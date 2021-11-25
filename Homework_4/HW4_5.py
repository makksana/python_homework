print('Task 5', end='\n\n')
# Используя модуль random и его функции randint 
# напишите игру "математика 5кл".

# Правила следующие. Есть три разных формулы 
# "y=2x+3" "y=3x+15" "y=x+7" 
# с помощю рандома выберите значение для х 
# в пределах от нуля до 30ти, и одну из формул. 
# Выведите на экран выбранную формулу и значение x, 
# получите ответ и проверьте его правильность 
# (для этого переведите свой ответ в строку и сравните строки). 
# Например х получил значение 5 и рандомная формула вторая. 
# Тогда на экран выводится

# y=3x+15
# x = 5
# y = ?
# если человек вводит 30 пишем ему "молодец" и заканчиваем игру. 
# Если другое число - "ты можешь лучше" и загадываем новое х и 
# новую формулу выбираем.


# Variant 1 
import random

number_of_attempts = 5
i = 0

while i < number_of_attempts:
    x = random.randint(0, 30)      
    formulas = ['2*x+3', '3*x+15', 'x+7']
    values = [2*x+3, 3*x+15, x+7]
    random_formula = random.randint(0,2)
    
    print(f'y={formulas[random_formula]}')
    print(f'x={x}')
    users_y = int(input('Какое значение будет иметь "y"? '))

    if users_y == values[random_formula]:
       print('Молодец!')
       break
    print('Ты можешь лучше')
    i+=1

# Variant 2   
# while i < number_of_attempts:
   
#     formulas = ['2*x+3', '3*x+15', 'x+7']
   
#     random_formula = random.choice(formulas)
#     x = random.randint(0, 30)

#     print(f'y={random_formula}')
#     print(f'x={x}')
#     y = eval(random_formula, {'x':x})
#     users_y = int(input('Какое значение будет иметь "y"? '))

#     if users_y == y:
#        print('Молодец!')
#        break
#     print('Ты можешь лучше')
#     i+=1
