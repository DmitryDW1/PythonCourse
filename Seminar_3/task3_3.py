'''
Задача No21.Напишите программу для печати 
всех уникальных значений в словаре
'''

list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
             {"VI": "S005"}, {"VII": " S005 "}, 
             {" V ":" S009 "}, {" VIII ":" S007 "}]
# unique_dict_items = set()
# for i in list_dict:
#     for j in i.keys():
#         unique_dict_items.add(i[j])
# print(unique_dict_items)
print(set([list(i.values())[0] for i in list_dict]))