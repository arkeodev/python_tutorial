class A:
    a = "I am a class attribute!"


if __name__ == "__main__":
    x = A()
    y = A()
    x.a = "This creates a new instance attribute for x!"
    print(y.a)
    # 'I am a class attribute!'
    print(A.a)
    # 'I am a class attribute!'
    A.a = "This is changing the class attribute 'a'!"
    print(A.a)
    # "This is changing the class attribute 'a'!"
    print(y.a)
    # "This is changing the class attribute 'a'!"
    # but x.a is still the previously created instance variable:
    print(x.a)
    # 'This creates a new instance attribute for x!'

    print(x.__dict__)
    # {'a': 'This creates a new instance attribute for x!'}
    print(y.__dict__)
    # {}
    print(A.__dict__)
    # dict_proxy({'a': "This is changing the class attribute 'a'!", '__dict__': < attribute '__dict__' of
    # 'A' objects >, '__module__': '__main__', '__weakref__': < attribute '__weakref__' of 'A' objects >,
    # '__doc__': None})
    print(x.__class__.__dict__)
    # dict_proxy({'a': "This is changing the class attribute 'a'!", '__dict__': < attribute '__dict__' of
    # 'A' objects >, '__module__': '__main__', '__weakref__': < attribute '__weakref__' of 'A' objects >,
    # '__doc__': None})
