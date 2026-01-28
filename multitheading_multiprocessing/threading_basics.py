import threading, time


def take_orders():
    for i in range(1, 4):
        print(f"Taking order for{i}")
        time.sleep(1)


def brew_chai():
    for i in range(1, 4):
        print(f"brewing chai for {i}")
        time.sleep(2)


# take two threads consider them as two waiters doing two diff works
# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)
order_thread.start()
brew_thread.start()
# wait for both to finish
order_thread.join()  # finish ur work and join us back
brew_thread.join()

print("all orders taken and brewed")
