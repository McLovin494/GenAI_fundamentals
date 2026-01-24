def process_order(item, qty):
    try:
        # trying to extract the key shorthand
        price = {"masala": 20}[item]
        cost = price * qty
        print(f"totoal cost is {cost}")
    except KeyError:
        print("Not on menu")
    except TypeError:
        print("qty must be in number")


process_order("ginger", 2)
process_order("masala", "two")
