# Association: Teacher and Classroom know each other

class Teacher:
    def __init__(self, name):
        self.name = name
        self.classroom = None


class Classroom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.teacher = None


teacher = Teacher("Mr. Santos")
classroom = Classroom("Room 101")

teacher.classroom = classroom
classroom.teacher = teacher

print(f"{teacher.name} teaches in {teacher.classroom.room_number}.")
print(f"{classroom.room_number} is taught by {classroom.teacher.name}.")