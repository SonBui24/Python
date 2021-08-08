def tribo(n):
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tribo(n - 1) + tribo(n - 2) + tribo(n - 3)

n = int(input("Nhập n: "))
print(f"Số Tribonacci của {n} là: {tribo(n)}")

def tribo(m):
    f = [1] * (m + 1)
    f[1] = f[2] = 1
    f[3] = 2
    for i in range(4, m + 1):
        f[i] = f[i - 1] + f[i - 2] + f[i - 3]
    return f[i]

m = int(input("Nhập m: "))
print(f"Số Tribonacci của {m} là: {tribo(m)}")
