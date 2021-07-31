from math import factorial
n = int(input("Nhập 1 số nguyên dương: "))
x = float(input("Nhập 1 số thực: "))
sum_s = 1
for a in range(1, n + 1):
    sum_s1 = sum_s + x ** a
print(f"S_1 = {sum_s1}")
for b in range(1, n + 1):
    if b % 2 == 0:
        sum_s2 = sum_s + x ** b
    else:
        sum_s2 = sum_s - x ** b
print(f"S_2 = {sum_s2}")
for c in range(1, n + 1):
    c_giaithua = factorial(c)
    sum_s3 = sum_s + x ** c / c_giaithua
print(f"S_3 = {sum_s3}")

"""
Phần S_3 mà viết sum_s3 = sum_s + x ** (c / c_giaithua) lại ra kết quả khác ạ
"""