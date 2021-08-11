list_ = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

n = len(list_)
count = 0
for i in range(n-1):
    for j in range(n+1, n):
        if list_[i] > list_[j]:
            count += 1

print(count)
