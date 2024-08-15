#1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('point')
print_params(2,0)
print_params('point', [23,111,8], False)
#print_params('point', [23,111,8], False, 'test') - не будет работать, тк задано больше аргкментов, чем может принять функция

print_params(b=25)
print_params(c=[1,2,3])

#2
values_list = ['string', 3.14, True]
values_dict = {'a': 'zero', 'b': [1, 'meinheim', False], 'c': 555}

print_params(*values_list)
print_params(**values_dict)
# print_params(*values_list, **values_dict) # - не будет работать, тк сумма элементов списка и словаря > кол-ва аргументов в функции



#3
values_list_2 = [2024, 'артефакт']
print_params(*values_list_2,42)



