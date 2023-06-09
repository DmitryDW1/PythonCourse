'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
за проезд и получали билет с номером. Счастливым билетом называют такой билет
с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется 
написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''
lucky_ticket = int(input('Введитер 6 цифр вашего билета: '))
while len(str(lucky_ticket)) != 6:
    lucky_ticket = int(input('Попробуйте ещё раз:'))
sum_left = 0
sum_right = 0
while lucky_ticket:
    number = lucky_ticket % 10
    if lucky_ticket > 999: sum_right += number
    else: sum_left += number
    lucky_ticket //= 10
if sum_right == sum_left: print(f'Ваш билет счастливый!!!', sum_left, '=', sum_right)
else : print('Неповезло...')