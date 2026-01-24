if True:
    try:
        if 1:
            chai_menu = {"masala": 20, "ginger": 40}
            print(chai_menu["elaichi"])
    except KeyError:
        print("Key does not exist")
    else:
        # this else is part of the try block not the if
        pass
