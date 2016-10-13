# First Example
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def succ(n):
    return n + 1

# Second Example
from math import sin, cos

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

# Third Example
def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            print("Argument is not an integer")

    return helper

@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Fourth example
class decorator2(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()

@decorator2
def foo():
    print("inside foo()")



if __name__ == "__main__":
    # Call first example
    succ(10)
    print("\n")

    # Call second example
    sin = our_decorator(sin)
    cos = our_decorator(cos)

    for f in [sin, cos]:
        f(3.1415)
    print("\n")

    # Call third example
    for i in range(1, 10):
        print(i, factorial(i))

    print(factorial(-1))
    print("\n")

    # Call fourth example
    foo()