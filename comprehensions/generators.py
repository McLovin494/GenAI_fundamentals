# generator is used for saving memory
# gives one item at a time....constant flow more like a stream comprehensions generate lists and all direclty in memory
# (expression for item in iterable if condition)
daily_sales = [5, 10, 12, 7, 3, 8, 9]
# items are given one my one
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)
