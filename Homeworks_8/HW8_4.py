print('Task 4', end='\n\n')
# Параметры по умолчанию
# Напишите функцию greet 
# принимающую имя name (type:str) 
# м слово word (type:str). 
# Если слово не передано 
# то считать его " -" и возвращающую строку вида 
# "[Имя] ты сегодня [слово]!"

# # todo: ваш код функции

# assert greet("111", "2") == "111 ты сегодня 2!"
# assert greet("игорь", "молодец") == "Игорь ты сегодня молодец!"
# assert greet(name="ольга", word="супер") == "Ольга ты сегодня супер!"
# assert greet("николай") == "Николай ты сегодня -!"

def greet(name:str, word:str='-') -> str:
    return f'{name.capitalize()} ты сегодня {word}!'

assert greet("111", "2") == "111 ты сегодня 2!"
assert greet("игорь", "молодец") == "Игорь ты сегодня молодец!"
assert greet(name="ольга", word="супер") == "Ольга ты сегодня супер!"
assert greet("николай") == "Николай ты сегодня -!"