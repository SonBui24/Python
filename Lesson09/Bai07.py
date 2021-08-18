input_s = 'Stringings'

set_s = set(input_s)
dict_s = {}
for i in set_s:
    dict_s[i] = input_s.count(i)
print(dict_s)
