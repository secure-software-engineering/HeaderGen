def func1():
    pass


def func2():
    pass


assign_1, assign_2 = func1, func2
assign_1()
assign_2() 

assign_1, assign_2 = func2, func1
assign_1()
assign_2()