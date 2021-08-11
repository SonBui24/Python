list_ = ['pip', 'pyp', 'sad', 'funny', 'a', 'v']

count = 0
for i in list_:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print(f"Số chuỗi có 2 ký tự trở lên và ký tự cuối giống ký tự đầu là: {count}")
