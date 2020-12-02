class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age  = age
        self.gpa  = gpa
    def updateGPA(self, newGPA):
        self.gpa = newGPA

def main():
    val  = Student("Alex", 21, 4.0)
    test = Student("Test", 18, 0)
    test.updateGPA(3.26)

main()

