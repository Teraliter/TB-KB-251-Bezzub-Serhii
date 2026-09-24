items = [1, 2, 3]
print("Initial:", items)

items.append(4)
print("append(4):", items)

items.extend([5, 6])
print("extend([5, 6]):", items)

items.insert(1, 99)
print("insert(1, 99):", items)

items.remove(99)
print("remove(99):", items)

items.sort()
print("sort():", items)

items.reverse()
print("reverse():", items)

copy_items = items.copy()
print("copy():", copy_items)

items.clear()
print("clear():", items)
