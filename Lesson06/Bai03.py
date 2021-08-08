def is_perfect(n):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False
