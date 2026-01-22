staff = [("amit", 22), ("zara", 20), ("Raj", 19)]
# how to print only if age >=18
# else runs if break is there fallback logic
for name, age in staff:
    if age <= 18:
        print("hired")
        break
else:
    print("not hired")
