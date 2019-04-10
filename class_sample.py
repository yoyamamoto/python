class Class_Sample:
    _var = ''

    def __new__(self):
        self._var = 'new'
    
    def __init__(self):
        self._var = 'init'
    
    def __del__(self):


