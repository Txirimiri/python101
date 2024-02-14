my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(key)

    items = list(my_dict.items())  # Convert items to a list for indexing
i = 0
while i < len(items):
    key, value = items[i]
    print(key, value)
    i += 1
