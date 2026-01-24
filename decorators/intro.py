from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("after functions runs")

    return wrapper()


@my_decorator
def greet():
    print("Hi from decorators class")
