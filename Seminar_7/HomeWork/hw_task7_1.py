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
def good_chant(text_chant):
    
        return sum(1 for i in text_chant if i in vowels)
    
def chars(text_chant):
    for i in text_chant:
        for j in i:
            if (chr(j) in vowels) and (chr(j+1) in vowels) in str(i):
                return True
text_chant = input().lower().split()
vowels = 'аеёиоуыэюя'
consonant = 'бвгджзклмнпрстфхцчшщ'
syllable = chars(i for i in text_chant)
chant = all([good_chant(i) == good_chant(text_chant[0]) for i in text_chant])
if chars(syllable and chant):
    print('Парам пам-пам')
else:
    print('Пам парам')