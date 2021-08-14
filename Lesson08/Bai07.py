my_tuple = (1, 2, 3, 'a', 'b')
your_tuple = (4, 5, 6, 'a', 'x')

a = False
for i in my_tuple:
    if i in your_tuple:
        a = True

print(a)
