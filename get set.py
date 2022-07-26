class Demo:
    def __init(self,name=0,add=0):
        self.__name=name
        self.__add=add
    def setname(self,name):
        self.__name=name
    def setadd(self,add):
        self.__add=add
    def getname(self):
        return self.__name
        
    def getadd(self):
        
        return self.__add
obj=Demo()
obj.setname("simar")
obj.setadd("model gram")
print(obj.getname())
print(obj.getadd())
