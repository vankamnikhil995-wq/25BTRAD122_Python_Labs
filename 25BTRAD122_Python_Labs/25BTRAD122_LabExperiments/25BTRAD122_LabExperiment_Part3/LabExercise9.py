
students = {}

number = int(input("Enter number of students: "))

for i in range(number):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"

    students[name] = {
        "Subject 1": mark1,
        "Subject 2": mark2,
        "Subject 3": mark3,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

print("\n===== STUDENT RESULTS =====")

for name, details in students.items():
    print("\nStudent Name:", name)
    print("Subject 1:", details["Subject 1"])
    print("Subject 2:", details["Subject 2"])
    print("Subject 3:", details["Subject 3"])
    print("Total Marks:", details["Total"])
    print("Average Marks:", round(details["Average"], 2))
    print("Grade:", details["Grade"])
