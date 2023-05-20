import time
start = time.time()

# list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
# count = 0
# for i in range(len(list_n)):
#     for j in range(i + 1, len(list_n)):
#         if list_n[j] == list_n[i]: count += 1
# print(count)

list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
count = [list_n[i] for i in range(len(list_n)) for j in range(i + 1, len(list_n)) if list_n[j] == list_n[i]]
print(count, len(count))


end = time.time()
print(end - start)