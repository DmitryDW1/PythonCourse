'''
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону (т.е. не 
меньше заданного минимума и не больше заданного 
максимума
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 
4, -2, 10, 2, 0, -9, 8, 10, -9, 
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''
x, y = int(input('Минимум: ')), int(input('Максимум: '))
list_nums = [int(input('Введите число: ')) for i 
             in range(int(input('Количество элементов массива: ')))]
list_index_nums = [i for i in range(len(list_nums)) if list_nums[i] in range(x, y)]
print(list_index_nums)


# nums_list = [int(i) for i in input().split()]
# num_min = int(input())
# num_max = int(input())

# print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])
# x, y = int(input('Минимум: ')), int(input('Максимум: '))
# list_nums = [-5, 9, 0, 3, -1, -2, 1, 4, 
#              -2, 10, 2, 0, -9, 8, 10, -9, 
#              0, -5, -5, 7]
# list_index_nums = [i for i in range(len(list_nums)) if list_nums[i] in range(x, y)]
# print(list_index_nums)