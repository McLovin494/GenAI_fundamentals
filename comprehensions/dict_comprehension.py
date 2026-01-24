tea_prices = {"masala chai": 40, "green tea": 50, "lemon tea": 200}
# way to read comprehensions are start from for loop
tea_prices_usd = {tea: price / 80 for tea, price in tea_prices.items()}
