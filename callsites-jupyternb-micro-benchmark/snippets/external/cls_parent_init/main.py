from pycg_external_module.ext import ParentInit

class A(ParentInit):
    def fn(self):
        self.parent_fun()


a = A()
a.fn()
