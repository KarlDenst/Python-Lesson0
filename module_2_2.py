first=int(input("введите любое число: "))
second=int(input("опять введите любое число: "))
third=int(input("снова введите любое число: "))

if first==second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)