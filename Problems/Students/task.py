class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.student_id = self.name[0] + self.last_name + self.birth_year

name = input()
last_name = input()
birth_year = input()

new_student = Student(name, last_name, birth_year)
print(new_student.student_id)
