a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))

if(a > b):
    max = a
else:
    max = b
if(c > max):
    max = c
print('Наибольшее число: ', max)