# import re
# string = 'h8i rajes34singh h4ow a23re yo76u abc67x'
# split_string = string.split()
# all_int = []
# for i in split_string:
#     num = int(re.search(r'\d+', i).group())
#     all_int.append(num)
# all_int.sort()

# final_list = []
# for nn in all_int:
#     # dd = [s for s in split_string if str(nn) in s and len(re.search(r'\d+', i).group()) == len(str(nn))]
#     for st in split_string:
#         if str(nn) in st and len(re.search(r'\d+', st).group()) == len(str(nn)):
#             final_list.append("".join(sorted(st)))
# result = " ".join(final_list)
# print "final result is :",result


# import bobo

# @bobo.query('/')
# def hello(name):
#     return 'Hello %s!' % name

# bobo -f test1.py


#-------------attrgetter---------

# metro_data = [
#  ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#  ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#  ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#  ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),  ]

# from collections import namedtuple
# LatLong = namedtuple('LatLong', 'lat long') 
# Metropolis = namedtuple('Metropolis', 'name cc pop coord')
# metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
# from operator import attrgetter
# name_lat = attrgetter('name', 'coord.lat')
# for city in sorted(metro_areas, key=attrgetter('coord.lat')):
#     print(name_lat(city))


# class Test:
#     cc = 8
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     # @staticmethod
#     # def foo(b):
#     #     c = Test.cc
#     #     return c

#     @classmethod
#     def create_from_list(cls, data):
#         return cls(data[0], data[1])
        

# obj = Test.create_from_list([3,4])
# # print obj.foo(6)
# print obj.a

#-----------------static method----
# class Test:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def _foo1(self):
#         return self.a
    
#     ee = property(_foo1)

#     @staticmethod
#     def foo():
#         return "static method parent"
    
#     @classmethod
#     def bar(cls):
#         return "class method parent"

# class Test1(Test):
#     # pass
#     def __init__(self):
#         self.a = 10

#     @staticmethod
#     def foo():
#         return "static method child"
    
   

# obj = Test1()
# print (obj.bar())

# obj = Test(10,7)
# print obj._foo1()

# obj = Test1()
# print (obj._foo1())


#---------------------

class A(object):
    pass
    # def foo(self):
    #     return "class A"
    

class B(object):
    def foo(self):
        return "class B"

class D(B):
    def foo(self):
        super(D, self).foo()
        return "class C"

class C(A,D):
    pass

obj = C()
print (obj.foo())
print (C.mro())

