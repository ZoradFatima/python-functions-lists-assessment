# Class Marks Analyzer
# This program takes students' names and marks and analyzes class results.


# This function asks for a valid number of students.
def get_student_count():
    while True:
        try:
            count = int(input("How many students are in the class? "))

            if count > 0:
                return count
            else:
                print("Please enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")


# This function asks for marks until the user enters a number from 0 to 100.
def get_valid_marks(student_name):
    while True:
        try:
            marks = int(input(f"Enter marks for {student_name} (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a whole number.")


# This function displays students who achieved the highest and lowest marks.
def show_highest_and_lowest(student_names, student_marks):
    highest_marks = max(student_marks)
    lowest_marks = min(student_marks)

    print(f"\nHighest Marks: {highest_marks}")
    print("Student(s) with highest marks:")

    for index in range(len(student_marks)):
        if student_marks[index] == highest_marks:
            print(f"- {student_names[index]}")

    print(f"\nLowest Marks: {lowest_marks}")
    print("Student(s) with lowest marks:")

    for index in range(len(student_marks)):
        if student_marks[index] == lowest_marks:
            print(f"- {student_names[index]}")


# This function displays the students who scored above the class average.
def show_above_average(student_names, student_marks, average):
    print("\nStudents Above Class Average:")

    found_student = False

    for index in range(len(student_marks)):
        if student_marks[index] > average:
            print(f"- {student_names[index]}: {student_marks[index]}")
            found_student = True

    if not found_student:
        print("No student scored above the class average.")


# -------------------- Main Program --------------------

print("\n===== CLASS MARKS ANALYZER =====")

# Create two separate lists to store names and marks.
student_names = []
student_marks = []

number_of_students = get_student_count()

# Ask for each student's name and marks.
for number in range(number_of_students):
    print(f"\nStudent {number + 1}")

    name = input("Enter student name: ").strip().title()
    marks = get_valid_marks(name)

    student_names.append(name)
    student_marks.append(marks)

# Calculate the class average.
total_marks = sum(student_marks)
class_average = total_marks / len(student_marks)

# Count passing and failing students.
passing_students = 0
failing_students = 0

for marks in student_marks:
    if marks >= 50:
        passing_students += 1
    else:
        failing_students += 1

# Display the class report.
print("\n" + "=" * 45)
print("              CLASS MARKS REPORT")
print("=" * 45)
print(f"Number of Students : {len(student_names)}")
print(f"Class Average      : {class_average:.2f}")
print(f"Passing Students   : {passing_students}")
print(f"Failing Students   : {failing_students}")

# Display highest and lowest marks, including ties.
show_highest_and_lowest(student_names, student_marks)

# Display students who scored above the average.
show_above_average(student_names, student_marks, class_average)

# Sort marks from highest to lowest.
sorted_marks = sorted(student_marks, reverse=True)

print("\nMarks from Highest to Lowest:")
for marks in sorted_marks:
    print(marks)

print("=" * 45)
