with open('test.txt', 'r', encoding='utf-8') as f:
    line1 = f.read()
with open('test1.txt', 'r', encoding='utf-8') as g:
    line2 = g.read()
with open('test2.txt', 'w', encoding='utf-8') as h:
    h.write(line1+line2)
