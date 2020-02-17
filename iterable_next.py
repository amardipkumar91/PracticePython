# import re
# import reprlib

# RE_WORD = re.compile("\w+")

# class Sentence:
#     def __init__(self, text):
#         self.text = text
#         self.word = RE_WORD.findall(text)
    
#     def __repr__(self):
#         return 'sentence(%s)'%reprlib.repr(self.text)
    
#     def __iter__(self):
#         return "hello"

#         return SentenceIterator(self.word)

# class SentenceIterator:
#     def __init__(self, word):
#         self.word = word
#         self.index = 0

#     def __next__(self):
#         try:
#             s_word = self.word[self.index]
#         except:
#             raise StopIteration()
#         self.index += 1
#         return s_word

#     def __iter__(self):
#         return self

# obj = Sentence("my name is amardip")
# for i in obj:
#     print (i)

#------------------------generator-----

# class Sentence:
#     def __init__(self, text):
#         self.text = text
#         self.word = RE_WORD.findall(text)
    
#     def __repr__(self):
#         return 'sentence(%s)'%reprlib.repr(self.text)
    
#     def __iter__(self):
#         for i in self.word:
#             yield i
#         return

# obj = Sentence("my name is amardip")
# for i in obj:
#     print (i)

from functools import wraps
def coroutine(func):
    @wraps(func)
    def primer(*arg, **kwrgs):
        gen = func(*arg, **kwrgs)
        next(gen)
        return gen
    return primer
@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
    
# avg = averager()
# next(avg)
# print (avg.send(10))
# print (avg.send(20))
# print (avg.send(30))



