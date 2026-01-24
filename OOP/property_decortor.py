# propertyd decorators are used to prevent changing it from others
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    # this is like getter and setter
    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Age must be betweem 1 and 5 years")


leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 4
print(leaf.age)
