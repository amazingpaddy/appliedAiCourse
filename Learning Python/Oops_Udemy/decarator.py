import time


def my_decarator(func):
    def wrapper(*args, **kwaras):
        print("I am decorating the functtion!!")
        func(*args, **kwaras)

    return wrapper


def my_decarator1(func):
    def wrapper(*args, **kwaras):
        print("I am decorating the functtion!!")
        return func(*args, **kwaras)

    return wrapper


@my_decarator
def hello(name):
    print(f"Hello {name}")


@my_decarator1
def hello1(name):
    return f"Welcome {name}"


# my_decarator(hello)()  instead of this functional call, we added decarator to the method - hello.
hello("Paddy")
print(hello1("Paddy"))


# Practical example ->  calculate timing of the function..
def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        fname = func.__name__
        print(f"Function - {fname} took {after - before} seconds to run to return the count - {value}")

    return wrapper


@timed
def sleep_sometime(seconds):
    time.sleep(seconds)


sleep_sometime(10)
