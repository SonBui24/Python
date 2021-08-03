s = input("Nhập chuỗi: ")
count = 0

for item in s:
    if "0" <= item <= "9":
        count += 1

print(f"Trong {s} có {count} ký tự số")