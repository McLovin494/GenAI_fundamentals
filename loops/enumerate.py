# why classic for loop fails
menu = ["Green tea", "Lemon Tea", "Spiced tea", "Mint tea"]
print(list(enumerate(menu)))
for idx, value in enumerate(menu, 1):
    print(f"{idx}-{value}")
