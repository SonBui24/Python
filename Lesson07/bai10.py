list_song = list(input("Nhập list bài hát: "))

a = []
for i in list_song:
    if i not in a:
        a.append(i)

print(a)
