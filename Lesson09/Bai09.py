Input = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Output = {}

for i in Input:
    item = i['item']
    amount = i['amount']
    if item in Output:
        Output[item] += amount
    else:
        Output[item] = amount
print(Output)
