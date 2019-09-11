class A(object):
    # def __init__(self):
    #     print "A init"

    def foo(self):
        print ("A")
    

class B(object):
    def __init__(self):
        print "B init"

    def foo(self):
        print "B"


class E(B):
    def __init__(self):
        super(E, self).__init__()
        print "E init"

    def foo(self):
        super(E, self).foo()
        print "E"
    
class D(A,E):
    pass

obj = D()
obj.foo()
print D.__mro__



## --------------Decorator ---------------
def test(func):
    def inner(*args, **kwargs):
        print "welcome"
        func(*args, **kwargs)
        
    return inner

@test
def test_deco():
    print "hi"
test_deco()

