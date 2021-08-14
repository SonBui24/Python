my_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]

list_hauto = []
for i in my_list:
    list_hauto.append(i.split('.')[-1])
print(f'Danh sách hậu tố của tên miền {list_hauto}')
