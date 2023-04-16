'''
Задача No23. Дан массив, состоящий из целых чисел. Напишите 
программу, которая подсчитает количество элементов массива, 
больших предыдущего (элемента с предыдущим номером)
'''

print('Введите несколько чисел: ')
numbers = [input() for i in range(5)]
# print(numbers)
# count = 0
# for i in range(len(numbers) - 1):
#     if numbers[i] < numbers[i + 1]: count += 1
# print(count) 
print(sum([numbers[i] > numbers[i - 1] for i in range(1, len(numbers))]))