minutes = int(input('Введите к-во минут: '))
hours = minutes // 60; 
minutes %= 60;  
print(hours,'час(а/ов)', minutes,'минут')