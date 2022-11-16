import math


def fakultaet(x):
    y = x
    if x < 0:
        return "Error, entered value has to be greaterequal zero."
    elif isinstance(x, float):
        return "Float not supported by this function"
    else:
        for i in range(1, x):
            y *= x - i

    return y


# Tests
print(f"fakultät von 5  = {fakultaet(5)}")
print(f"fakultät von 7  = {fakultaet(7)}")
print(f"fakultät von 20 = {fakultaet(20)}")
print(f"fakultät von 12 = {fakultaet(12)}")
print(f"fakultät von 3  = {fakultaet(3.32)}")
print(f"fakultät von 2  = {fakultaet(2)}")
print(f"fakultät von 5  = {fakultaet(-5)}")
print(f"fakultät von 5  = {fakultaet(0)}")

