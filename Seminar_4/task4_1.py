'''
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
каждый символ уже встречался. Количество повторов добавляется к символам с помощью 
постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию split()
'''



list_user = input('Введите символы строки через пробел: ').split()  
out_dict = {}   
print(list_user)                                                   
for i in list_user:                                                
    if i in out_dict:                                              
        print(f'{i}_{out_dict[i]}', end='  ')
    else:
        print(i, end='  ')
    out_dict[i] = out_dict.get(i, 0) + 1
#print(out_dict)                               

'''
string = "a a a b c a a d c d d".split()

dict = {}.fromkeys(string, 0)

for i in string:
    print(f"{i}_{dict[i]}" if dict[i] else i, end=" ")
    dict[i] += 1
'''