#D- Data Structures



def display():

    print("\nStudent Information")

    print("1. Add Student")

    print("2. View Students")

    print("3. Update Student")

    print("4. Delete Student")

    print("5. Exit")



def add(students):

    name = input("Enter student name: ")

    age = int(input("Enter student age: "))

    grades = input("Enter student grades : ")

    students[name] = {"age": age, "grades": grades}

    print(f"Student '{name}' added successfully.")



def view(students):

    if not students:

        print("No students found.")

        return

    print("\nStudent List:")

    for name, details in students.items():

        print(f"- Name: {name}, Age: {details['age']}, Grades: {details['grades']}")



def update(students):

    name = input("Enter the name of the student to update: ")

    if name in students:

        print(f"Current Data: Age: {students[name]['age']}, Grades: {students[name]['grades']}")

        age = int(input("Enter new age (or press Enter to keep current): ") or students[name]['age'])

        grades = input("Enter new grades (press Enter to keep current): ")

        students[name] = {"age": age, "grades": grades}

        print(f"Student '{name}' updated successfully.")

    else:

        print(f"Student '{name}' not found.")



def delete(students):

    name = input("Enter the name of the student to delete: ")

    if name in students:

        del students[name]

        print(f"Student '{name}' deleted successfully.")

    else:

        print(f"Student '{name}' not found.")



def main():

    students = {}

    while True:

        display()

        choice = input("Enter your choice: ")

        if choice == "1":

            add(students)

        elif choice == "2":

            view(students)

        elif choice == "3":

            update(students)

        elif choice == "4":

            delete(students)

        elif choice == "5":

            print("Exiting the program.")

            break

        else:

            print("Invalid choice. Please try again.")



if __name__ == "__main__":

    main()
