# := this is walrus operator
# x=5 assignment anything that returns is expression
# value = 13
# remainder = value % 5
# if remainder:
#     print("Not divisible")

value = 13
if remainder := value % 5:
    print("Not divisible")
