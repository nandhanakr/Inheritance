#Single Inheritance :
# When a child class inherits only a single parent class.

class Parent:                  #Parent class/ Main class/ Base class
    def first(self):
        print('first program')
class Child(Parent):
    def second(self):           #Child class/ Sub class/ Derived class
        print('second program')
ob = Child()
ob.first()
ob.second()