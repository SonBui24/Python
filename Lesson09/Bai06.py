my_dict = {
    1: 5,
    2: 4,
    3: 3,
    4: 2
}

a = sorted(my_dict.values())
b = a[-3:]
c = set()
for i, o in my_dict.items():
    if o in b:
        c.add((i, o))
print(c)
