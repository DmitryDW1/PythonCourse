'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий
по величине элемент к заданному числу X. Пользователь в первой 
строкев водит натуральное число N – количество элементов в 
массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
'''

numbers = [input('Введите несколько чисел: ') for i in range(int(input('Введите количество элементов в массиве:')))]
print(numbers)
x = input('Введите искомое число x: ')
for i in range(len(numbers)):
    for j in range(i):
        if numbers[i] < x:
            numbers[j] = numbers[i]
print(numbers[j])