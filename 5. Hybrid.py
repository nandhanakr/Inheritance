#Hybrid inheritance :
#combination of different types of inheritance
#such as multiple inheritance and single inheritance.
class Office:
    def office_data(self):
        print("Office details here")
class Emp1(Office):
    def emp1_data(self):
        print("Employee 1 details here")
class Emp2:
    def emp2_data(self):
        print("Employee 2 details here")
class Emp3(Emp1, Emp2):
    def emp3_data(self):
        print("Employee 3 details here")

obj = Emp3()
obj.office_data()
obj.emp1_data()
obj.emp2_data()
obj.emp3_data()