first_purchase = int(input('Введите цену за 1 товар: '))
second_purchase = int(input('Введите цену за 2 товар: '))
third_purchase = int(input('Введите цену за 3 товар: '))

total_sum = first_purchase + second_purchase + third_purchase

if(total_sum > 10000):
    print('Цена со скидкой составит: ', total_sum - total_sum / 10)
else:
    print('Скидки не будет, цена: ', total_sum)
    