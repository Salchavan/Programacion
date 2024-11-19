class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
        self.degree = degree
        
    def printDegree(self):
        print(f"{self.name} is in {self.degree}º")

print("Enter the name, age and degree of the student: ")
name = input("Name: ")
age = input("Age: ")
degree = input("Degree: ")
print(F"""
    Dates of the student:
    
    Name {name}
    Age: {age}
    Degree: {degree}""")
student1 = Student(name, age, degree)
student1.printDegree()