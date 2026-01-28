import time


def brewchai():
    print("Brewing chai")
    time.sleep(2)  # takes 2 seconds
    print("Chai ready")


def toast_bread():
    print("Toasting bread")
    time.sleep(2)  # also 2 seconds
    print("Bread ready")


# Run synchronously
start = time.time()

brewchai()
toast_bread()

end = time.time()
print(f"Total time: {end - start:.2f} seconds")
