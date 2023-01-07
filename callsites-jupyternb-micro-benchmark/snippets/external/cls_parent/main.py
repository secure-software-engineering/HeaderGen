from pycg_external_module.ext import Parent

class A(Parent):
    def fn(self):
        self.parent_fun()


a = A()
a.fn()
