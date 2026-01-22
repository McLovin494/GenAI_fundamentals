# mutable
# holds distinct data just like the maths set
essential_spices = {"cardamom", "ginger", "cinnamom"}
optional_spices = {"cloves", "ginger", "black pepper"}
all_spices = essential_spices | optional_spices
print(all_spices)
common_spices = essential_spices & optional_spices
print(common_spices)
only_in_essential = essential_spices - optional_spices

print(only_in_essential)

# same membership test
