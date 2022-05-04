class Student:               #Create a class using keyword 'class' space classname then colon
    def __init__(self, name):         ## Use the init method inside the class using 'def __init__' then put in the object name within parenthesis
        self.name = name          ##Create a method using 'objectname.propertname' then = 'value', in this case we use the above parameter 'name' as the properties' value.
                                       ##The above line basically just says 'whenever you call the .name property, you are calling the 'name paramter' value'.
        self.grades = (90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)




student = Student("Bob")        ##This is use using the 'name' paramter when we made the class, and we are telling python that paramter equals "Bob" in this object.
print(student.average_grade())
print(student.name)
