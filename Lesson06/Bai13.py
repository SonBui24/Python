def find_x(list_a, x):
    for i in range(len(list_a)):
        if list_a[i] == x:
            print(i, end=" ")


print(find_x("sdfsdgsdfsghsdf", "d"))
