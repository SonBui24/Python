my_list = [1, 2, 3, 4, (1, 2, 3), 4, 5]

count = 0
for i in my_list:
    if isinstance(i, tuple):
        break
    count += 1

print(count)
