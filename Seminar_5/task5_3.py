'''
Задача No35. Напишите функцию, которая принимает одно число и проверяет, является
ли оно простым Напоминание: Простое число - это число, которое имеет 2 делителя: 1
и n(само число)
Input: 5
Output: yes
'''

def easy_number(number):
    if number < 2: return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0: return False
    return True
number = (int(input('Введите число: ')))
if easy_number(number): print('Yes')
else: print('No')