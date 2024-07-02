#2
immutable_var=8,True,[4,9,'string-0'],'string-1'
print(immutable_var)
#3
immutable_var[2][1]=6 #обращение к списку внутри кортежа - элементы в списке можно изменять
immutable_var[2][2]=False

#immutable_var[0][0]=3 #при обращении к 1-му элементу(8) кортежа - ошибка - тк нельзя изменять элемент кортежа
#4
mutable_list=['space','rainbow',1984, True]
mutable_list[0]='earth'
mutable_list[2]='vogue'
print(mutable_list)