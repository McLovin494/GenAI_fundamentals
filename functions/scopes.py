def order():
    sam_order = "pasta"

    def john_order():
        print("sam_order", sam_order)
        tracy_order = "pizza"
        print("tracy_order", tracy_order)

    john_order()


order()
