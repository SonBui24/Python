from math import factorial
epsilon = float(input("Nhập số nhỏ hơn 1: "))

i = 0
tong = 0
i_gt = factorial(i)

while (1 / i_gt) >= epsilon:
    tong = tong + (1 / i_gt)
    i = i + 1
    i_gt = factorial(i)

print(f"e = {tong}")
