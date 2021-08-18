my_dict = {
    1: 2,
    2: 3,
    3: 4,
    4: 5
}
your_dict = {
    4: 6,
    6: 7,
    7: 8,
    1: 2,
    2: 3
}

a = set()

for i, o in my_dict.items():
    if i in your_dict and o == your_dict[i]:
        a.add((i, o))
print(a)
