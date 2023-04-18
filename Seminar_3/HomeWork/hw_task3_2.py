'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий
по величине элемент к заданному числу X. Пользователь в первой 
строкев водит натуральное число N – количество элементов в 
массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
'''

numbers = [int(input('Введите несколько чисел: ')) for i in range(int(input('Введите количество элементов в массиве:')))]
print(numbers)
x = int(input('Введите искомое число x: '))
near_max = len(numbers) - len(numbers)                      
for i in range(0, len(numbers) - 1):
    if numbers[i] < x and numbers[i] > near_max:
        near_max = numbers[i]
print(near_max)

# near_max = [abs(numbers[i] - x) for i in range(len(numbers))]
# print(numbers[near_max.index(min(near_max))])