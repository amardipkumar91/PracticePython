# class CustomDict(dict):
#     def __init__(self,data):
#         self.data = data
#         super(CustomDict, self).__init__()

#     def __str__(self):
#         return str(self.data) 
        
#     def __getitem__(self, key):
#         return self.data[key]
    
#     def __setitem__(self, key, val):
#         self.data.update({key : val})
   

# abc = {'a':4, 'b' :5}
# obj = CustomDict(abc)
# print obj['a']
# obj['e'] = 9
# print obj

#--------------__missing__--------------


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self(str(key))
    
    def get(self, key, default = None):
        try:
            return self[key]
        except:
            return default
    
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = {4:5}
obj = StrKeyDict0(d)
print obj
print obj.get('6')