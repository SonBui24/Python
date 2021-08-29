n = int(input("nhập vào n : "))

with open('test.txt', 'r', encoding='utf-8') as f:
    for i in range(n):
        line = f.readline().rstrip("\n")
        print(f'Dòng {i+1}: {line}')
