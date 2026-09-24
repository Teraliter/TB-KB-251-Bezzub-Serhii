data = {"a": 1, "b": 2, "c": 3}
print("Initial:", data)

data.update({"d": 4, "e": 5})
print("update:", data)

print("keys:", list(data.keys()))
print("values:", list(data.values()))
print("items:", list(data.items()))

del data["a"]
print("del data['a']:", data)

data.clear()
print("clear:", data)
