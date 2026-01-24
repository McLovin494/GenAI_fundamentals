def local_chai():
    yield "Masala chai"
    yield "Ginger chai"


def imported_chai():
    yield "Matcha"
    yield "Oolong"


def full_menu():
    # similar to import from
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("Stall closed")


stall = chai_stall()
print(next(stall))
# always close the generators
stall.close()
