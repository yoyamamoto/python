# coding :utf-8
from pprint import pprint

class Class_Sample:
    _var = 'member'

    def __new__(self):
        print('new')
        #pprint(self)
    
    def __init__():
        print('init')

    
    def __del__(self):
        print('del')

    def __str__(self):
        print('str')

class Class_Sub(Class_Sample):
    pass

"""
    Class_Sample() # output new
    sub = Class_Sub() # output new
    pprint(sub.__init__) # <function Class_sample.__init__ at 0x039AF780>
"""

test = Class_Sample

pprint(test)

