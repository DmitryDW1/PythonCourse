'''
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод: 
пара-ра-рам рам-пам-папам па-ра-па-дам 
Вывод:
Парам пам-пам
'''
# def good_chant(text):
    
#         return sum(1 for i in text if i in 'аеёиоуыэюя')
    
# text_chant = input().lower().split()
# ritm = good_chant(text_chant[0])

# if all([ritm(i) == ritm for i in text_chant]):

#     print('Парам пам-пам')
# else:
#     print('Пам парам')

'''
answer = [len(list(filter(lambda x: x in 'аеёиоуыэюя', chant))) for chant in input()lower().split()]
print('Парам пам-пам' if all(x == answer[0] for x in answer) else 'Пам парам')
'''

def good_chant(text_chant):
        return sum(1 for i in text_chant if i in vowels)
    
text_chant = input().lower().split()
vowels = 'аеёиоуыэюя'
if all([good_chant(i) == good_chant(text_chant[0]) for i in text_chant]):
    print('Парам пам-пам')
else: print('Пам парам')