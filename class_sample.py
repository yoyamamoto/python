class Class_Sample():
    _var = 'member'

    def __new__(self):
        self._var = 'new'
    
    def __init__(self):
        self._var = 'init'
    
    def __del__(self):
        return 'delete' + self._var

    def __str__(self):
        return 'printした時に実行される特殊関数' + self._var

# これクラスを直接プリントできるんだけどどういう事なんだ。
print(Class_Sample())
