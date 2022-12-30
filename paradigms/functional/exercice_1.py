#Transform all list items to uppercase

items = ['car', 'airplan', 'bus', 'bike', 'rocket']

newItems = list(map(lambda item: item.upper(), items))

print(newItems)