# code duplication
# explicit call
# super
class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         # explicit constructor call
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # access to the parent class
        # becuase this is base class constructor and it does not have the spice level
        super().__init__(type_, strength)
        self.spice_level = spice_level
