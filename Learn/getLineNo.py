
from inspect import currentframe

def lno():
    cf = currentframe()
    val = str(cf.f_back.f_lineno)+". "
    return val

print "this is Me", lno()
print lno(), "Hi! there"

