class Student:
    """A class representing a student."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getAge(self):
        return self.age

class IEStudent(Student):
    """A class extending student class to IE students."""
    def __init__(self, name, age, dept):
        # call __init__ for student
        Student.__init__(self, name, age) 
        self.dept = dept
    
    def getAge(self): 	# redefines getAge method entirely
        return self.age
    
def main():
    ie_student = IEStudent("John", 30, "Industrial Engineering")
    print("Name:", ie_student.name)
    print("Age:", ie_student.age)
    print("Dept:", ie_student.dept)
    
main()




