import math

x = float(input("Nhập giá trị x:"))
y = float(input("Nhập giá trị y:"))
z = float(input("Nhập giá trị z:"))

F = (x + y + z) / (x**2 + y**2 + 1) - abs(x - z * math.cos(y))
print("Giá trị của F:", F)
