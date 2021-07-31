from math import factorial
epsilon = float(input("Nhập số nhỏ hơn 1: "))
n = 0
tong = 1
i_gt = 1
while (1 / i_gt) >= epsilon:
    n = n + 1
    i_gt = factorial(n)
    tong = tong + (1 / i_gt)
print(f"e = {tong}")
