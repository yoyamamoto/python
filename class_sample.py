# coding :utf-8
from pprint import pprint

class Class_Sample:
    _var = 'member'

    def __new__(self):
        print('new')
        pprint(self)
    
    def __init__(self):
        print('init')
    
    def __del__(self):
        print('del')

    def __str__(self):
        print('str')

#class Class_sub(Class_Sample):


# これクラスを直接プリントできるんだけどどういう事なんだ。
Class_Sample()

