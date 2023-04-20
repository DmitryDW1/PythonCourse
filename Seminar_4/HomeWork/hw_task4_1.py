'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во 
элементов второго множества. Затем пользователь вводит сами элементы множеств
'''

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
numbers_n = list(int(input('Введите элемент первого множества: ')) for i in range(n))
print(numbers_n)
numbers_m = list(int(input('Введите элемент второго множества: ')) for i in range(m))
print(numbers_m)

print('Общие элементы множеств: ', (sorted(set(numbers_n).intersection(set(numbers_m)))))

'''
Эталонное решение

mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
print(i, end=' ')

'''