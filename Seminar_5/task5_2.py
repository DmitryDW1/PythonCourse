'''
Задача No33. Хакер Василий получил доступ к классному журналу ихочет  заменить  все 
свои  минимальные  оценки  на максимальные.   Напишите   программу,   которая
заменяет   оценки   Василия,   но   наоборот:   все максимальные – на минимальные.
Input:5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

import random
def max_min(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 3: numbers[i] = 1
    return numbers
numbers = [int(random.randint(1, 5)) for i in range(int(input('Введите количество оценок: ')))]
print(numbers)
print(f'Заменили оценки:))) {max_min(numbers)}')