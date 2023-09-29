hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))

earned_money = ((200*hours)/(2**3)) + hours

if(earned_money < credit + food):
    print('Часов не хватает. Придётся работать больше!')
else:
    print('Часов хватает. Можно отдохнуть')