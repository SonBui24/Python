while True:
    n = int(input("Nhập số nguyên dương nhỏ hơn 1000: "))
    if 0 < n < 1000:
        tong = 0
        while 0 < n < 1000:
            tong = tong + n % 10
            n = int(n / 10)
        print(f"Tổng các chũ số của n: {tong}")
        break
    print("Nhập sai. Vui lòng nhập lại")
