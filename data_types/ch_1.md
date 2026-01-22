`sugar_amount = 3
temp=3
print(f"Initial sugar amount is {sugar_amount}")

# sugar_amount = 13

# print(f"Second sugar amount is {sugar_amount}")

# we only changed the reference of sugar_amount 3 was always there

# confirm using print id

print(f"id of temp {id(temp)} and id of sugar amount {id(sugar_amount)}")`
#<-------->

## What do we conclude?

- Things like numbers 2 , 5 these are immutable their existence in memory cannot be erased only reference can be changed
- However things like set() are mutable means objects can be changed
