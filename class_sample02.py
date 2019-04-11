# coding :utf-8

class Class_Sample02:
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


test = Class_Sample02

