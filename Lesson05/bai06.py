s = str(input("Nhập chuỗi bất kỳ: "))
i = str(input("Nhập ký tự bất kỳ từ chuỗi: "))

for a in range(len(s)):
    if s[a] == i:
        print(a, end=" ")
