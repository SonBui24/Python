list_ = [1, 2, 3, 4, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6]
a = int(input("Nhập đọo dài phần đầu: "))

l1 = list_[:a]
l2 = list_[a:]

print(f"Phần đầu: {l1}, \nPhần sau: {l2}")
