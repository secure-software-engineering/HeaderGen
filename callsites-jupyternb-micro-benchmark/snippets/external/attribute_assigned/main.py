from pycg_external_module.ext import Cls

def fn(a):
    a()

a = Cls()

fn(a.fun)
