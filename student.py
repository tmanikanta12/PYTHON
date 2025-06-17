class Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def display_details(self):
        print("Student Details:")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Department :", self.department)
        print()

# First student
s1 = Student("Mani", 1203, "CSE")

# Second student
s2 = Student("Ravi", 1204, "ECE")

# Display both students
s1.display_details()
s2.display_details()

