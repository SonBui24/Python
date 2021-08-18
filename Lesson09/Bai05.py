sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]

a = {i: sampleDict[i] for i in keys}

print(a)

b = {}
for o in keys:
    b[o] = sampleDict[o]
print(b)
