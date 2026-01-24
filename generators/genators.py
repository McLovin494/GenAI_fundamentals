def serve_chai():
    yield "Cup 1:Masala chai"
    yield "Cup 2:Elaichi chai"
    yield "Cup 3:Ginger chai"


# now stores the refernce to the definiton
stall = serve_chai()
print(stall)
# code eexecutes only when this code runs


for cup in stall:
    # calculating the first value only after that it pauses in next naxt then next value
    print(next(cup))
