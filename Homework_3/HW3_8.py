print('Task 8', end='\n\n')

# Используя функцию input получаем от пользователя строку. 
# Напишите код в котором просим дать ответ на загадку. 
# Если человек сдается он вводит q или Q и прерываем цикл while. 
# Если угадал - выводим поздравление. Если нет - пристыдите его. 
# Ответ принимается регистронезависимо.

# question = 'Маленькое беленькое на потолко висит не светит'
# answer = 'лампачка'
# #todo: ваш код с циклом и условием выхода

answer = 'лампачка'
number_of_attempts = 5
i = 0

while i < number_of_attempts:
    question = input('Маленькое беленькое на потолко висит не светит (если сдаешься введи q или Q): ')
    if question.lower() == 'q':
        print('Очень жаль, что не захотел угадать мою загадку')
        break
    else:
        if question.lower() == answer:
            print('Это правильный ответ!')
            break
        else:
            print('Ты ошибся')
    i+=1
    continue


