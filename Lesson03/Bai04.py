a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
if (a + b) > c or (a + c) > b or (b + c) > a:
    if a ** 2 == (b ** 2 + c ** 2) or b ** 2 == (a ** 2 + c ** 2) or c ** 2 == (a ** 2 + b ** 2):
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác")
else:
    print("Đây không phải tam giác")
