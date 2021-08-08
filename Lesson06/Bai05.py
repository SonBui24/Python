def count_upper_lower(str_):
    count_upper = 0
    count_lower = 0
    for i in str_:
        if i.isupper():
            count_upper += 1
        if i.islower():
            count_lower += 1
    return count_lower, count_upper
