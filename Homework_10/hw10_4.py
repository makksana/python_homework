print('Task 4', end='\n\n')
# Атрибуты экземпляра класса
# Задача
# Создайте класс Friend 
# для хранения имени name и телефона phone. 
# Обратите внимание, у друга может не быть телефона.

# class Friend:
#     # todo: ваш код тут
#     pass

# u1 = Friend("Андрей", "+380331233333")
# u2 = Friend("Петр", )

# assert hasattr(u1, "name")
# assert hasattr(u1, "phone")
# assert u1.name == "Андрей"
# assert u2.name == "Петр"
# assert u1.phone == "+380331233333"
# assert u2.phone == ""

class Friend:
    
    def __init__(self, name, phone=''):
        self.name = name
        self.phone = phone

u1 = Friend("Андрей", "+380331233333")
u2 = Friend("Петр", )

assert hasattr(u1, "name")
assert hasattr(u1, "phone")
assert u1.name == "Андрей"
assert u2.name == "Петр"
assert u1.phone == "+380331233333"
assert u2.phone == ""