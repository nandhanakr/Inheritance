class Student:
    def __init__(self):
        self.Name=" "           #empty string declaration
        self.Age=" "
        self.Place=" "
    def Stud_data(self):
        self.Name=input("Enter Student Name:")
        self.Age=int(input("Enter Student Age:"))
        self.Place=input("Enter Student Place:")
    def display_student(self):
        print("STUDENT DETAILS")
        print("Student Name:",self.Name)
        print("Student Age:",self.Age)
        print("Student Place:",self.Place)
obj=Student()
obj.Stud_data()
obj.display_student()
