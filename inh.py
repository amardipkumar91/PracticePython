class Test(object):
    def __init__(self):
        self._a = 10
    
    def dispaly(self):
        return self._a
    
    def __display1(self):
        self._a

class Test1(Test):
    def __init__(self):
        super().__init__()
        self.b = 20

    def foo(self):
        return self._a, self.b

obj = Test1()
import pdb;pdb.set_trace()