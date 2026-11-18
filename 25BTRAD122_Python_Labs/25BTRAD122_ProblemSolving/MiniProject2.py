number = int(input("Enter number of students: "))

for i in range(number):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")
    total = 0

    for j in range(3):
        mark = float(input("Enter marks for Subject " + str(j + 1) + ": "))
        total = total + mark

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

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Total Marks:", total)
    print("Average:", average)
    print("Grade:", grade)
