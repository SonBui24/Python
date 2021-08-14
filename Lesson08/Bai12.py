my_set = {0, 1, 2, 3, 4, 5, 6}
your_set = {5, 6, 7, 8, 9, 0, 1}
my_set.difference_update(your_set)
print(my_set)

my_set = {0, 1, 2, 3, 4, 5, 6}
your_set = {5, 6, 7, 8, 9, 0, 1}
my_set.intersection_update(your_set)
print(my_set)

my_set = {0, 1, 2, 3, 4, 5, 6}
your_set = {5, 6, 7, 8, 9, 0, 1}
my_set.isdisjoint(your_set)
print(my_set)

my_set = {0, 1, 2, 3, 4, 5, 6}
your_set = {5, 6, 7, 8, 9, 0, 1}
my_set.issubset(your_set)
print(my_set)

my_set = {0, 1, 2, 3, 4, 5, 6}
your_set = {5, 6, 7, 8, 9, 0, 1}
my_set.issuperset(your_set)
print(my_set)

my_set = {0, 1, 2, 3, 4, 5, 6}
your_set = {5, 6, 7, 8, 9, 0, 1}
my_set.symmetric_difference_update(your_set)
print(my_set)
