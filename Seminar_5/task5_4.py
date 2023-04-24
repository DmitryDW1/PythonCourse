'''
Задача No37. Дано натуральное число N ипоследовательность 
из N элементов. Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input:    2 -> 3 4
Output: 4 3
'''

def list_up(n, m):
    if n == m:
        return 
    print(n + 1, end = " ")
    list_up(n + 1, m)
    
def list_down(n, m):
    if n == m:
        return 
    print(m, end = " ")
    list_down(n, m - 1)

n = (int(input('Введите число: ')))
m = n * 2
list_up(n, m)
print()
list_down(n, m)