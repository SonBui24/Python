my_string = input("Nhập một đoạn văn: ")

maxx = list_word[0]
for i in list_word:
    if len(i) > len(maxx):
        maxx = i

print(maxx)
