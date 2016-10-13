def f():
    global s
    print(s)
    s = "I love London!"
    print(s)

s = "I love Paris in the summer!"
f()
