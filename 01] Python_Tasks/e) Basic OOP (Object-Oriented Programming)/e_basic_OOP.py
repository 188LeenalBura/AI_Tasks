class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

student = Student("Alice", 19, [85, 90, 95])
student.display_details()
print(f"Average Grade: {student.calculate_average()}")

student = Student("Daniel", 21, [70, 90, 45])
student.display_details()
print(f"Average Grade: {student.calculate_average()}")

student = Student("David", 20, [89, 97, 78])
student.display_details()
print(f"Average Grade: {student.calculate_average()}")
