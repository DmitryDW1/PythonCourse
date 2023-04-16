'''
Задача 20:В настольной игре Скрабл (Scrabble) каждая буква имеет
определенную ценность. В случае с английским алфавитом очки 
распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите  программу,  которая  вычисляет  стоимость  введенного  
пользователем  слова. Будем считать, что на вход подается только 
одно слово, которое содержит либо только английские, либо только
русские буквы.
'''

lang = bool(input('Английский = 0 Русский  = любая кнопка: '))
text = input('Введите слово: ').upper()
sum = 0
if lang:
    ru = {1 : 'А, В, Е, И, Н, О, Р, С, Т',
          2 : 'Д, К, Л, М, П, У',
          3 : 'Б, Г, Ё, Ь, Я',
          4 : 'Й, Ы',
          5 : 'Ж, З, Х, Ц, Ч',
          8 : 'Ш, Э, Ю',
          10 : 'Ф, Щ, Ъ'}
    for i in text:
        for k, v in ru.items():
            if i in v:
                sum = sum + int(k)
    print(sum)
else:
    en = {1 : 'A, E, I, O, U, L, N, S, T, R',
          2 : 'D, G',
          3 : 'B, C, M, P',
          4 : 'F, H, V, W, Y',
          5 : 'K',
          8 : 'J, X',
          10 : 'Q, Z'}
    for i in text:
        for k, v in en.items():
            if i in v:
                sum = sum + int(k)
    print(sum)
if sum == 0: print('Вы неправильно указали язык')
# import re
# def isCyrillic(text):
# 	return bool(re.search('[а-яА-Я]', text))
# points_en = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# text = input().upper()
# if isCyrillic(text):
# 	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
# else:
# 	print(sum([k for i in text for k, v in points_en.items() if i in v]))