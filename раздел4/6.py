guest_roll = int(input('Кубик гостя: '))
barkeeper_roll = int(input('Кубик владельца: '))

if(guest_roll >= barkeeper_roll):
    print('Разность', guest_roll - barkeeper_roll)
    print('Игрок платит \nИгра окончена')
else:  
    print('Сумма', guest_roll + barkeeper_roll)
    print('Владелец платит \nИгра окончена')