feedback = {}

number = int(input("Enter number of students: "))

print("\n===== STUDENT CLASSROOM FEEDBACK SURVEY =====")
print("1. Excellent")
print("2. Good")
print("3. Average")
print("4. Poor")

for i in range(number):
    print("\nStudent", i + 1)
    response = input("Enter your feedback: ").strip().title()

    if response in feedback:
        feedback[response] += 1
    else:
        feedback[response] = 1

print("\n===== FEEDBACK REPORT =====")

for response, count in feedback.items():
    print(response, ":", count, "students")

print("\n===== SURVEY ANALYSIS =====")

most_common = max(feedback, key=feedback.get)

print("Total responses:", number)
print("Most selected feedback:", most_common)
