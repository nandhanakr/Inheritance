class Parent:
    def parent_data(self):
        print("Parent details")
class Child(Parent):
    def child_data(self):
        super().parent_data()
        print("Child Details")
ob = Child()
ob.child_data()