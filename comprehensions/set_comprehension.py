recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"],
}
# we are looking for unique spices that is why spice is used
#               here
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
