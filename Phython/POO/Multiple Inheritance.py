class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Language:
    def __init__(self, language):
        self.language = language

class Student(Language, Person):
    def __init__(self, name, age, language, curse, subject, notes):
        Person.__init__(self, name, age)
        Language.__init__(self, language)
        self.curse = curse
        self.subject = subject
        self.notes = notes

person1 = Student("luis", 18, "English", "6to", "mathematics", "9")

print(person1.language)

