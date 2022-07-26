from abc import ABC,abstractmethod
class Student(ABC):
    @abstractmethod
    def f1(self):
        pass
class Test(Student):
    def f1(self):
        print("hi")
obj=Test()
obj.f1()
