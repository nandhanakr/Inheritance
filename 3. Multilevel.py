#Multilevel Inheritance :
# When a child class becomes a parent class for another child class.
class Parent:
    def parent_data(self):
        print("Parent details are here")
class Child1(Parent):
    def child1_data(self):
        print("Child1 details are here")
class Child2(Child1):
    def child2_data(self):
        print("Child2 details are here")
ob = Child2()
ob.parent_data()
ob.child1_data()
ob.child2_data()