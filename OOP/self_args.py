class ChaiCup:
    size = 150

    def describe(self):
        return f"The size of the cup is {self.size}"


masala_tea = ChaiCup()
print(masala_tea.describe())
print(ChaiCup.describe(masala_tea))
