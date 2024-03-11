class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
#Equality Method (2%)
    def __eq__(self, equality):
        return self.name == equality.name
#Less Than Method (2%)
    def __lt__(self, less):
        return self.name < less.name
#Greater Than Method (2%)
    def __ge__(self, greater):
        return self.name >= greater.name
#Results
    def display(self):
        print(f"Name: {self.name}\nScore: {self.number}\n")
      
#Main Function (4%)
def main():
    students = [
        Student("Santiago Cruz", 4.0),
        Student("Mark Johnson", 3.3),
    ]

    students.sort()

    for student in students:
        student.display()

if __name__ == "__main__":
    main()