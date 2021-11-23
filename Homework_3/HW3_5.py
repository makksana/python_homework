print('Task 5', end='\n\n')

# У вас есть переменные holiday, day_of_week, wallet 
# проставьте условия в код. 
# попробуйте менять исходные значения чтоб убедиться что все

holiday, day_of_week, wallet = False, 6, 5000
if holiday == True or day_of_week == 6 and wallet == 0:
    print("оно то и можно погулять но не на что")
elif holiday == False or day_of_week == 6 and 0 < wallet < 200:
    print("пиво и чипсы на большее денег нет")
elif holiday == True or day_of_week == (5, 6, 7) and wallet >= 5000:
    print("гуляем в ресторане, всех угощаю")
elif wallet > 5000:
    print("После Безоса следующим лечу я. И моя любимая кошка!")
else:
    print("работаем")
