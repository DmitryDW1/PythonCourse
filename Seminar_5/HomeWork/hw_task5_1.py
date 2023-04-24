'''
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и 
возводит число А в целую степень B с помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

# def degree(a, b, res):
#     if b == 0: 
#         print('А в степени В: ', res)
#         return
#     res = res * a
#     degree(a, b - 1, res)
# a = (int(input('Введите число А: ')))
# b = (int(input('Введите число B: ')))
# degree(a, b, res = 1)

def degree(a, b):
    if b == 1: return a
    if b < 0: return 1 / (a * degree(a, - b - 1))
    return a * degree(a, b - 1)
a = int(input('Введите число А: '))
b = int(input('Введите степень B: '))
print('А в степени В: ', degree(a, b))