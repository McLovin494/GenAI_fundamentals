chai_type = "Plain"


# using global we can access the global variables
def front_desk():
    def kitchen():
        global chai_type
        chai_type = "mango"
        print(f"updated chai type {chai_type}")

    kitchen()


front_desk()
