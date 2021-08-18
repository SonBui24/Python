my_dict = {
    1: 2,
    2: 3,
    3: 4,
    4: 5
}
minn = my_dict[1]
maxx = my_dict[1]
for i in my_dict:
    if my_dict[i] > maxx:
        maxx = my_dict[i]
    if my_dict[i] < minn:
        minn = my_dict[i]

print(maxx)
print(minn)
