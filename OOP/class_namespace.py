class Chai:
    # properties
    origin = "India"


print(Chai.origin)
# properties can be added like this too
Chai.is_hot = False
print(Chai.is_hot)
# creating objects from class Chai

masala = Chai()
print(masala.is_hot)
masala.is_hot = "i dunno"
print("for masala object", masala.is_hot)
print(f"for chai object{Chai.is_hot}")
