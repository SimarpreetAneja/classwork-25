class Demo:
    _a=47
class B(Demo):
    
        def __init__(self):
            super(). __init__()
            _a=46
            print(self._a)
obj=B()

