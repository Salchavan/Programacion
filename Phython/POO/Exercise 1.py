class StudentClass:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def studying(self):
        print(f"The student {self.name} is studying...")

name = input("Enter your name: ")
age = input("Enter your age: ")
grade = input("Enter your grade: ")

student = StudentClass(name, age, grade)
print(f"""
    Student Data:
    Name: {student.name}
    Age: {student.age}
    Grade: {student.grade}
    """)

while True:
    n = input(">> ")
    if (n.lower() == "study"):
        student.studying()