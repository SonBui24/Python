list_ = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]

most_char = 0
most_count = 0
for char in list_:
    count_char = list_.count(char)
    if most_count < count_char:
        most_count = count_char
        most_char = char

print(f"Giá trị xuất hiện nhiều nhất: {most_char} \nSố lần xuất hiện: {most_count}")
