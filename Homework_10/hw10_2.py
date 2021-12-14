print('Task 2', end='\n\n')
# Doggy age

# Create a class Dog 
# with class attribute `age_factor` equals to 7. 
# Make __init__() 
# which takes values for a dog’s age. 
# Then create a method `human_age` 
# which returns the dog’s age in human equivalent.

class Dog:
    ageFactor = 7

    def __init__(self, dogs_age):
        self.dogs_age = dogs_age

    def humanAge(self):
        return  Dog.ageFactor * self.dogs_age

dog1 = Dog(13)

print(dog1.humanAge())