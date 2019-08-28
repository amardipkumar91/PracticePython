# class Test(object):
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, number):
#         return self.n + number
    

# num = Test(10)
# print (num + 5)


#-------------

# class Test(object):
#     def __foo(self):
#         print " I am A class Method"
    
#     def foo(self):
#         self.__foo()
    
# obj = Test()
# obj.foo()

#------------

# class A(object):
#     def __foo(self):
#         print " I am A class Method"
    
#     def foo(self):
#         self.__foo()

# class B(A):
#     def __foo(self):
#         print "I am B class Method"

# obj = A()
# obj.foo()