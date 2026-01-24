# syntax
# [expression for item in iterable if condition]
candidates = ["Mclovin", "John Cena", "Kick"]

print([print(item) for item in candidates if item == "Mclovin"])
menu = ["tea", "pizza", "coffee", "pasta", "burgers"]
order = [item for item in menu if item == "tea" or item == "pizza"]
print(order)
