# Иван Васильевич пришел на рынок и решил купить
# два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза
'''
n = int(input())

weight = int(input())
max_weight = weight
min_weight = weight

for _ in range(n-1):
    weight = int(input())
    if max_weight < weight:
        max_weight = weight
    elif min_weight > weight:
        min_weight = weight

print(f"{min_weight} {max_weight}")
'''

num = int(input())
heavy = 0
light = 1000

for i in range(num):
    weight = int(input())
    if weight > heavy:
        heavy = weight
    if weight < light:
        light = weight

print(light, heavy)