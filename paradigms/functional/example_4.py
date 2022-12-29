listExample = [1, 1, 2, 3, 5, 8, 13]
print(f"List Example: {listExample}")

listMap = map(lambda item : item * 3, listExample)
print(f"List Map: {list(listMap)}")


listFilter = filter(lambda item: item % 2 != 0, listExample)
print(f"List Filter: {list(listFilter)}")