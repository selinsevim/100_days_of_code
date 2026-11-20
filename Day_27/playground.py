# Unlimited positional arguments
def add(*args):
    print(args)  # this prints tuple
    print(args[0])  # indexing gives the first tuple element, position matters
    sum = 0
    for num in args:
        sum += num
    return sum


# it can take as many as arguments without defining in the function
print(add(3, 4, 5, 6, 7))


# Keyword arguments
def calculate(n, **kwargs):
    # basically it is dictionary
    # print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    # alternatively
    # print(kwargs["add"])
    # print(kwargs["multiply"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # you make it optional
        self.model = kw.get(
            "model"
        )  # with get if it is not defined in the object, it returns None


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
