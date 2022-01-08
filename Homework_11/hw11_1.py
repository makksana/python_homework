print('Task 1', end='\n\n')
# School

# Make a class structure in python 
# representing people at school. 
# Make a base class called Person, 
# a class called Student, 
# and another one called Teacher. 
# Try to find as many methods and attributes 
# as you can which belong to different classes, 
# and keep in mind which are common and which are not. 
# For example, 
# the name should be a Person attribute, 
# while salary should only be available to the teacher.


class Person:
    def __init__(self, firstname, lastname, age, sex):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex


class Student(Person):
    def __init__(self, firstname, lastname, age, sex, visited_lessons):
        Person.__init__(self, firstname, lastname, age, sex)
        self.visited_lessons = visited_lessons

    def info(self):
        print("Student", self.firstname, self.lastname, self.age, "years old has visited", self.visited_lessons, "lessons")


class Teacher(Person):
    def __init__(self, firstname, lastname, age, sex, salary, work_experience):
        Person.__init__(self, firstname, lastname, age, sex)
        self.salary = salary
        self.work_experience = work_experience

    def display(self):
        print("Teacher", self.firstname, self.lastname, self.age, "years old earns", self.salary, "per month.", self.sex, "has", self.work_experience, "years of working experience")

student1 = Student('Harry', 'Potter', 12, 'He', 7)
student2 = Student('Hermione', 'Granger', 13, 'She', 10)
teacher1 = Teacher('Severus', 'Snape', 59, 'He', 1500, 32)

student1.info()
student2.info()
teacher1.display()