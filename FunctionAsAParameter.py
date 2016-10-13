# First example:
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")


def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    print("func's real name is " + func.__name__)
    func()


# Another example:
import math

def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

if __name__ == "__main__":
    # Call first example
    f(g)

    # Call second example
    print("\n")
    print(foo(math.sin))
    print(foo(math.cos))
