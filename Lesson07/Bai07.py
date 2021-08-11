list1 = ['s', 'b', 1, 2, 3]
list2 = ['s', 'c', 4, 5, 6]

a = False
for i in list1:
    if i in list2:
        a = True

print(a)
