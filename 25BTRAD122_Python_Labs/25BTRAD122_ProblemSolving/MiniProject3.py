students = []

while True:
    print("\n===== ATTENDANCE TRACKER =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Update Attendance")
    print("4. Display Attendance")
    print("5. Calculate Attendance Percentage")
    print("6. Identify Low Attendance Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")

        student = {
            "name": name,
            "attendance": []
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == 2:
        name = input("Enter student name: ")

        for student in students:
            if student["name"].lower() == name.lower():
                status = input("Enter status (P/A): ").upper()

                if status == "P" or status == "A":
                    student["attendance"].append(status)
                    print("Attendance marked successfully!")
                else:
                    print("Invalid attendance status!")
                break
        else:
            print("Student not found!")

    elif choice == 3:
        name = input("Enter student name: ")

        for student in students:
            if student["name"].lower() == name.lower():
                print("Attendance records:", student["attendance"])

                day = int(input("Enter attendance number to update: "))

                if 1 <= day <= len(student["attendance"]):
                    status = input("Enter new status (P/A): ").upper()

                    if status == "P" or status == "A":
                        student["attendance"][day - 1] = status
                        print("Attendance updated successfully!")
                    else:
                        print("Invalid status!")
                else:
                    print("Invalid attendance number!")
                break
        else:
            print("Student not found!")

    elif choice == 4:
        print("\n===== ATTENDANCE DETAILS =====")

        for student in students:
            print("\nStudent:", student["name"])
            print("Attendance:", student["attendance"])

    elif choice == 5:
        print("\n===== ATTENDANCE PERCENTAGE =====")

        for student in students:
            total = len(student["attendance"])
            present = student["attendance"].count("P")

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            print(student["name"], ":", round(percentage, 2), "%")

    elif choice == 6:
        threshold = float(input("Enter attendance threshold: "))

        print("\n===== LOW ATTENDANCE STUDENTS =====")

        for student in students:
            total = len(student["attendance"])
            present = student["attendance"].count("P")

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            if percentage < threshold:
                print(student["name"], ":", round(percentage, 2), "%")

    elif choice == 7:
        print("Exiting Attendance Tracker!")
        break

    else:
        print("Invalid choice! Try again.")
