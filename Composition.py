# Composition: School owns its SchoolLibrary

class SchoolLibrary:
    def open_library(self):
        print("The school library is open.")


class School:
    def __init__(self):
        self.library = SchoolLibrary()


school = School()
school.library.open_library()