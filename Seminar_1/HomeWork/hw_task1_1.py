'''
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''

number = int(input('Введите трёзначное число: '))
while len(str(number)) != 3:
    number = int(input('Непрвильно! попробуйте ещё раз:'))
sum_number = 0
while number:
    sum_number += number % 10
    number //= 10

print('Сумма цифр в числе равна: ', sum_number)