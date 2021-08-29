strs = input("nhập vào chuỗi bạn cần thêm: ")

with open("test.txt", 'a', encoding='utf-8') as f:
    f.write("\n" + strs)
