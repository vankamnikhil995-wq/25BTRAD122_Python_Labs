import json

filename = "students.json"


def load_students():
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("The student file is empty or contains invalid data.")
        return []


def save_students(students):
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)


while True:
    students = load_students()

    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Display All Students")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            roll_no = input("Enter roll number: ").strip()

            if any(s["roll_no"] == roll_no for s in students):
                print("Roll number already exists!")

            else:
                name = input("Enter student name: ").strip()
                course = input("Enter course: ").strip()

                if not roll_no or not name or not course:
                    print("All fields are required!")

                else:
                    student = {
                        "roll_no": roll_no,
                        "name": name,
                        "course": course
                    }

                    students.append(student)
                    save_students(students)
                    print("Student added successfully!")

        elif choice == 2:
            roll_no = input("Enter roll number to search: ").strip()

            for student in students:
                if student["roll_no"] == roll_no:
                    print("\nStudent Found!")
                    print("Roll Number:", student["roll_no"])
                    print("Name:", student["name"])
                    print("Course:", student["course"])
                    break
            else:
                print("Student not found!")

        elif choice == 3:
            roll_no = input("Enter roll number to update: ").strip()

            for student in students:
                if student["roll_no"] == roll_no:
                    name = input("Enter new name: ").strip()
                    course = input("Enter new course: ").strip()

                    if name and course:
                        student["name"] = name
                        student["course"] = course
                        save_students(students)
                        print("Student details updated!")
                    else:
                        print("Name and course cannot be empty!")
                    break
            else:
                print("Student not found!")

        elif choice == 4:
            print("\n===== STUDENT RECORDS =====")

            if len(students) == 0:
                print("No student records available.")

            else:
                for student in students:
                    print("\nRoll Number:", student["roll_no"])
                    print("Name:", student["name"])
                    print("Course:", student["course"])

        elif choice == 5:
            print("Exiting Student Data Manager!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid menu number!")

    except PermissionError:
        print("Permission denied while accessing the file.")

    except OSError as e:
        print("File error:", e)
