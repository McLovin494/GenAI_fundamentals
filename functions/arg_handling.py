chai = "ginger_tea"


def prepare_chai(order):
    print("Preparing", order)


prepare_chai(chai)

chai = [1, 2, 3]


def edit_cup(cup):
    cup[1] = 42


edit_cup(chai)
print(chai)


def prepare_tea(*ingredients):
    for item in ingredients:
        print(item)


prepare_tea("milk", "water", "tea_leaves", "sugar")


def pizza(*essential, **extras):
    print("Essentials", essential)
    print(f"White chocolate {extras["white_chocolate"]}")


pizza("Dough", "Sauces", "Cheese", white_chocolate="Hersheys")


def chai_order(order="Hitesh"):
    print(order)
