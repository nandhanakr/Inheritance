# Multiple Inheritance :
# When a child class inherits from more than one parent class.
class Parent1:
    def parent1_details(self):
        print("Parent1 details here")
class Parent2:
    def parent2_details(self):
        print("Parent2 details here")
class Child(Parent1, Parent2):
    def Child_details(self):
        print("Child details here")

ob = Child()
ob.parent1_details()
ob.parent2_details()
ob.Child_details()