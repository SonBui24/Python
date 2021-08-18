my_dict = {
    1: 2,
    2: 3,
    3: 4,
    4: 5
}
a = sorted(my_dict)
b = a[-3:]

for i in b:
    print(f'{i} : {my_dict.get(i)}')
