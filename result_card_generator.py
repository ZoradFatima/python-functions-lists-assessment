# Student Result Card Generator
# This program takes one student's details and prints a result card.


# This function asks for marks until the user enters a number from 0 to 100.
def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a whole number.")


# This function calculates the percentage.
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


# This function returns a grade according to the percentage.
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# This function removes extra spaces and makes each name word start with a capital letter.
def format_name(name):
    return name.strip().title()


# -------------------- Main Program --------------------

print("\n===== STUDENT RESULT CARD GENERATOR =====")

# Get and clean the student's name.
student_name = format_name(input("Enter student name: "))

# Get a roll number containing digits only.
while True:
    roll_number = input("Enter roll number: ").strip()

    if roll_number.isdigit():
        break
    else:
        print("Invalid roll number! Use digits only.")

# Get marks in five subjects.
subjects = ["English", "Mathematics", "Computer", "Physics", "Chemistry"]
marks_list = []

for subject in subjects:
    marks = get_valid_marks(subject)
    marks_list.append(marks)

# Calculate total marks and percentage.
total_marks = sum(marks_list)
maximum_marks = 500
percentage = calculate_percentage(total_marks, maximum_marks)

# Find the grade from the percentage.
grade = get_grade(percentage)

# A student must get at least 40 marks in every subject to pass.
if any(mark < 40 for mark in marks_list):
    final_status = "Fail"
else:
    final_status = "Pass"

# Show the result card using f-strings.
print("\n" + "=" * 40)
print("              STUDENT RESULT CARD")
print("=" * 40)
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("-" * 40)

for index in range(len(subjects)):
    print(f"{subjects[index]:<15}: {marks_list[index]} / 100")

print("-" * 40)
print(f"Total Marks  : {total_marks} / {maximum_marks}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
print(f"Final Status : {final_status}")
print("=" * 40)
