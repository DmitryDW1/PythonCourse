# list_1 = []
# list_1 = list()
# list_1 = [1, 9, 8, 33, 89]
# print (list_1)
# print (*list_1)
# for i in list_1:
#     print(i, end = " ")
# print('\n', len(list_1))
# print(list_1[0])
# print(list_1[1])
# print(list_1[-1])
# print(list_1[-2])
# list_1.append(8)
# print(list_1)
# list_1.append(9)
# print(list_1)
# list_2 = []
# for i in range(5):
#     list_2.append(i)
#     print(list_2)
# print(list_2.pop())
# print(list_2)
# print(list_2.pop())
# print(list_2)
# print(list_2.pop())
# print(list_2)
# print(list_2.pop())
# print(list_2)
# print(list_2.pop())
# print(list_2)

# # Удаление конкретного элемента
# list_3 = [12, 7, -1, 21, 0]
# print(list_3.pop(0)) # 12
# print(list_3)

# # Добавление элемента на нужную позицию
# list_3 = [12, 7, -1, 21, 0]
# print(list_3.insert(2, 11))
# print(list_3)

# Срез списка

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print (list_1[0]) # 1
# print (list_1[1]) # 2
# print (list_1[-1]) # 10
# print (list_1[-5]) # 6
# print (list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print (list_1[:2]) # [1, 2]
# print (list_1[len(list_1)-2:]) #[9, 10]
# print (list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print (list_1[6:-18]) # []
# print (list_1[0:len(list_1):6]) # [1, 7]
# print (list_1[::6]) # [1, 7]

# Кортежи

# t = ()
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990,)
# print(type(t))
# v = [1, 8, 9]
# print(v)
# print(type(v))
# v = tuple(v)
# print(v)
# print(type(v))
# a, b, c = v
# print(a, b, c)
# colors = ['red', 'green', 'blue']
# print(colors)
# t = tuple(['red', 'green', 'blue'])
# print(t[2])
# print(t[0])
# for e in t:
#     print(e)
# # t[0] = 'black'
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)# {'up':'↑', 'left':'←', 'down':'↓','right':'→'}
print(dictionary['left'])# ←
# типы ключей могут отличаться
print(dictionary['up'])# ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left'])# ⇐
#print(dictionary['type'])# KeyError: 'type'
del dictionary['left']# удаление элемента
for item in dictionary:# for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →