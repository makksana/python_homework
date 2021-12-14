print('Task 5', end='\n\n')
###Задача 
# Напишите класс который будет "рисовать" букву псевдографикой. 
# Например чтобы диезами написать букву 
# A нам нужно напечатать

 ###
#  #
####
#  #
# Реализуйте класс SymbolA с методам line 
# который параметром принимает номер выводимой строки и 
# возвращает соответствующее строковое значение.

class SymbolA:
    def __init__(self, element):
        self.element = element
        self.lines = [
            ' '+self.element*3,
            self.element + '  ' + self.element,
            self.element*4,
            self.element + '  ' + self.element
        ]

    def line(self, number):
        return self.lines[number] 

a = SymbolA('@')
assert a.line(0) == " @@@"
assert a.line(1) == "@  @"
assert a.line(2) == "@@@@"
assert a.line(3) == "@  @"

a2 = SymbolA('$')
assert a2.line(0) == " $$$"
assert a2.line(1) == "$  $"
assert a2.line(2) == "$$$$"
assert a2.line(3) == "$  $"