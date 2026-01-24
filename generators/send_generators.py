def chai_customer():
    print("Welcome !what chai would u like")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield


stall = chai_customer()
next(stall)  # starting point of the genrator
stall.send("Masala Chai")
# does not execute unless u send value to the yield
