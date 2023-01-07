def func1():
    pass


def func2():
    pass


def func3():
    pass


def func4():
    pass


def func5():
    pass


def func6():
    pass


a, (b, c) = func1, (func2, func3)
a()
b()
c()

a, (b, c) = func4, (func5, func6)
a()
b()
c()