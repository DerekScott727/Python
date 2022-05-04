class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)




student = Student("Bob", (100, 90, 93, 78, 90))        ##This is use using the 'name' paramter when we made the class, and we are telling python that paramter equals "Bob" in this object.

student2 = Student("Joe", (100, 91, 88, 44, 25))

print(student.average_grade())
print(student.name)

print(student2.average_grade())
