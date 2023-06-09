'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно 
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''

n = int(input('Введите количество монеток, лежащих на столе: '))
i = 1
heads = 0
tails = 0
while i <= n:
    coin = int(input('Какой стороной лежит монетка(герб - 0, остальное - решка)? '))
    if coin == 0: heads += 1
    else: tails += 1
    i += 1
if heads > tails:
    print(f'Нужно перевернуть {tails}')
else: print(f'Нужно перевернуть {heads}')