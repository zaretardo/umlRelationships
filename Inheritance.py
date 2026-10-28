# Inheritance: Student is a Person

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")


student = Student("Maria")
student.introduce()
student.study()