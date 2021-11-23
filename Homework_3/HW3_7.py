print('Task 7', end='\n\n')

# Провалидируйте введенный пользователем номер телефона.

# начинается с +3
# код оператора один из 050 067 099 063
# длинна правильная попробуйте менять значение номера 
# чтоб убедиться что ваши условия отрабатывают правильно.
# phone = '+321123456123'
# # ваш код

# rezulting_string = sample_string[0:2]+sample_string[-2]+sample_string[-1]

phone_number = input('Enter your phone number, exemple +32112345612: ')
if len(phone_number)==12 and phone_number[2:13].isnumeric() and phone_number[0] == '+' and phone_number[1] == '3':
    print(f'{phone_number} is a valid phone number')
else:
    print(f'{phone_number} is not a phone number')