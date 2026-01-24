class Chai:
    temperature = "hot"
    strength = "strong"


cutting = Chai()
cutting.temperature = "cold"
print(cutting.temperature)
print(Chai.temperature)
# falls back to the class one
# if no fall back it gives error
del cutting.temperature

print(cutting.temperature)
