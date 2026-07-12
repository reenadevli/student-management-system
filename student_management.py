students = []


def add_student():
    print("\n----- Add Student -----")

    name = input("Enter Student Name: ")

    try:
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return

        student = {
            "Name": name,
            "Age": age,
            "Marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    except ValueError:
        print("Invalid input!")


def view_students():
    print("\n----- Student List -----")

    if not students:
        print("No students found.")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['Name']}")
        print(f"   Age: {student['Age']}")
        print(f"   Marks: {student['Marks']}")
        print("-" * 30)


def search_student():
    name = input("\nEnter student name to search: ")

    found = False

    for student in students:
        if student["Name"].lower() == name.lower():
            print("\n Student Found")
            print(f"Name : {student['Name']}")
            print(f"Age : {student['Age']}")
            print(f"Marks : {student['Marks']}")
            found = True
            break

    if not found:
        print("Student not found.")


def delete_student():
    name = input("\nEnter student name to delete: ")

    for student in students:
        if student["Name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Selected student not found.")


while True:
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")