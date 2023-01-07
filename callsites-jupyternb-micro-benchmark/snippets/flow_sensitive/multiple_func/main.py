def func1():
    pass


def func2():
    func1()


a = func2

a()


def func2():
    pass


a = func2

a()
