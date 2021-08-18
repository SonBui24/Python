a = (input("Nhập một đoạn văn: ")).split(" ")

dict_count = {}
for i in a:
    dict_count[i] = a.count(i)

print(dict_count)
