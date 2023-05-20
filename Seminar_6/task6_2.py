# list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
# list_k = [i for i in range(1, len(list_n) - 1) if (list_n[i - 1] and list_n[i + 1]) < list_n[i] in list_n]
# print(list_k)

list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
list_k = [i for i in range(1, len(list_n) - 1) if list_n[i - 1] < list_n[i] > list_n[i + 1]]
print(list_k)