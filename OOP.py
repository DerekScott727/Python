class Student:               #Create a class using keyword 'class' space classname then colon
    def __init__(self):         ## Use the init method inside the class using 'def __init__' then put in the object name within parenthesis
        self.name = "rolf"           ##Create a method using 'objectname.propertname' then = 'value'. ('.name' is called a property)
                                       ##The above line basically just says 'whenever you call the .name property, you are calling the 'rolf' value'


student = Student()     ## Making the new 'student' variable into an object of the Student class by using equal sign
print(student.name)    ### Calling the student variable with the .name property which we know has the value of "rolf"
