#2 словари
my_dict={'Skywalker':1977,'Yoda':1001,'DarthVeder':1952,'Eniken':2001}
print(my_dict)
print(my_dict['Skywalker'])
print(my_dict.get('Trade_Federation','no such key found'))
my_dict.update({'Grivus':1941,'Sith':1939})
y=my_dict.pop('Yoda')
print(y)
print(my_dict)

#3 множества
my_set={4,9,8,3.14,8,2,0,4,7,'viola',(9,2,1),'ketchup','viola'}
print(my_set)
my_set.update({(2,4,16),'tabasco'})
my_set.remove((9,2,1))
print(my_set)







