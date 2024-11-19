from abc import ABC, abstractclassmethod
class Person(ABC):
    @abstractclassmethod
    def __init__(self, name, age, gender, activity):
        self.name = name
        self.age = age
        self.gender = gender
        self.activity = activity
    
    @abstractclassmethod
    def makeActivity(self):
        pass 
    def present(self):
        print(f"Hello i am {self.name} whit {self.age}, i am {self.gender}")
        
class Student(Person):
    def __init__(self, name, age, gender, activity):
        super().__init__(name, age, gender, activity)
        
    def makeActivity(self):
        print(f"I am studying {self.activity}")
        
class Teacher(Person):
    def __init__(self, name, age, gender, activity):
        super().__init__(name, age, gender, activity)
        
    def makeActivity(self):
        print(f"I am teaching {self.activity}")
        
        
student = Student("Salva", "16", "Male", "Programming")
student.present()
student.makeActivity()
teacher = Teacher("Ale", "45", "Male", "Programming")
teacher.present()
teacher.makeActivity()