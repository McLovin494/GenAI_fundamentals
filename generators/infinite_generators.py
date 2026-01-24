def inifinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1


refill = inifinite_chai()
for _ in range(3):
    print(next(refill))
