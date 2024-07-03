#Hierarchical Inheritance :
# Hierarchical inheritance involves multiple inheritance from the same base or parent class.
class Vehicle:
    def Vehicle_data(self):
        print("Parent details")
class Car(Vehicle):
    def car_data(self):
        print("Child1 details")
class Bike(Vehicle):
    def bike_data(self):
        print("child2 details")
ob1 = Car()
ob1.car_data()
ob1.Vehicle_data()
ob2=Bike()
ob2.bike_data()
ob2.Vehicle_data()

