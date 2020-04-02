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


#-------------Count of total anagram substrings--------------------
def countOfAnagramSubstring(s): 
    n = len(s) 
    mp = dict() 
    for i in range(n): 
        sb = '' 
        for j in range(i, n):   
            sb = ''.join(sorted(sb + s[j])) 
            mp[sb] = mp.get(sb, 0) 
            mp[sb] += 1
    anas = 0
    for k, v in mp.items(): 
        anas += (v*(v-1))//2
    return anas 
s = ["aa", "aa", "dog", "god"]
print(countOfAnagramSubstring(s))

