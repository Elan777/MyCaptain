class Student:
 
  # Constructor
    def __init__(self, name, age, m1, m2):
        self.name = name
        self.age = age
        self.m1 = m1
        self.m2 = m2
 
    # Function to create and append new student
    def accept(self, Name, age, marks1, marks2):
   
  # use ' int(input()) ' method to take input from user
        ob = Student(Name, age, marks1, marks2)
        ls.append(ob)
 
    # Function to display student details
    def display(self, ob):
        print("Name : ", ob.name)
        print("Age : ", ob.age)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")
 
    # Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].age == rn):
                return i
 
    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
 
    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].age = roll

ls = []
obj = Student('', 0, 0, 0)
 
print("\nOperations:")
print("\n1.Accept Student details\n2.Display Student Details")
 
obj.accept("Ram", 18, 100, 100)
obj.accept("Sita", 20, 90, 90)
obj.accept("Ravan", 21, 80, 80)
 
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
