# static methods cannot initialize
# only one constructor but we can mimick multiple
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # always return in classmethod
    @classmethod
    # no self it gets cls ie class reference
    def from_dict(cls, order_data):
        return cls(order_data["tea_type"], order_data["sweetness"], order_data["size"])

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)


order1 = ChaiOrder.from_dict(
    {"tea_type": "masala tea", "sweetness": "medium", "size": "large"}
)
order2 = ChaiOrder.from_string("ginger-lowsugar-small")
print(order1, order2)
