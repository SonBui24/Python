from math import sqrt

print("Giải phương trình bậc 2")
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
delta = b ** 2 - 4 * a * c

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm duy nhất: x = 0")
        else:
            print(f"Phương trình có 1 nghiệm duy nhất: x = {-c/b}")
else:
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print(f"Phương trình có 1 nghiệm duy nhất: x = {-b / (2 * a)}")
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print(f"x1 = {float((-b - sqrt(delta)) / (2 * a))}")
        print(f"x2 = {float((-b + sqrt(delta)) / (2 * a))}")

"""Làm bài này e phải ổn lại kiến thức :|
    E import math vào k đc a ạ. Nó hiện import math như 1 dòng comment
"""