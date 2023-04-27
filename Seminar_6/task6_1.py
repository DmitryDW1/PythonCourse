list_n = [input() for i in range (input('Введите количество элементов списка n: '))]
list_m = [input() for i in range (input('Введите количество элементов списка m: '))]
list_k = [i for i in list_n if i not in list_m]
print (list_k)