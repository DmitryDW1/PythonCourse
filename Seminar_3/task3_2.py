'''
Задача No19. Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
на K элементов вправо,  K – положительное число.
'''
print('Введите несколько чисел: ')
numbers = [input() for i in range(5)]
print(numbers)
print('На сколько элементов нужно сдвинуть список? ')
k = int(input())
for i in range(k):
    numbers.insert(0, numbers.pop())
print(numbers)
