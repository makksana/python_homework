print('Task 3', end='\n\n')
# Виключення
# Напишите функцию которая будет переводить 
# возраст с Земного на Марсианский. 
# В году на Земле 365 дней а на марсе 687

# def mars_age(age: int) -> int:
#     pass


# assert mars_age(10) == 5
# assert mars_age(63) == 33
# assert mars_age(1000) == 531

EARTH_YEAR_IN_DAYS=365
MARSIAN_YEAR_IN_DAYS=687

def mars_age(age: int) -> int:
    earth_days = age*EARTH_YEAR_IN_DAYS
    marsian_years = earth_days//MARSIAN_YEAR_IN_DAYS
    return marsian_years

assert mars_age(10) == 5
assert mars_age(63) == 33
assert mars_age(1000) == 531