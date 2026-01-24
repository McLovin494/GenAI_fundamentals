class ChaiOrder:

    # constructor via init initializatin
    def __init__(self, type_, size):

        # variables can be created like this too
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} "


order = ChaiOrder("Masala Chai", 200)
print(order.summary())
