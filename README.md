# Python Functions and Lists Assessment

## Project Overview

This project contains two beginner-friendly Python programs. They practise functions, string handling, lists, loops, input validation, and basic calculations.

## Program 1: Student Result Card Generator

File: `result_card_generator.py`

This program:
- Takes a student's name and roll number.
- Takes marks in five subjects.
- Checks that the roll number contains digits only.
- Checks that every subject mark is between 0 and 100.
- Calculates total marks and percentage.
- Finds the grade using the assessment grading scale.
- Gives a final Fail status if any subject mark is below 40.
- Prints a formatted result card.

## Program 2: Class Marks Analyzer

File: `class_marks_analyzer.py`

This program:
- Asks how many students are in the class.
- Stores names in `student_names` and marks in `student_marks`.
- Checks that each mark is between 0 and 100.
- Calculates the class average.
- Displays the highest and lowest marks and all students who achieved them.
- Counts passing students (50 or above) and failing students (below 50).
- Displays students who scored above the class average.
- Displays marks from highest to lowest.

## Python Concepts Used

- Functions: `def`, parameters, and `return`
- String methods: `strip()`, `title()`, and `isdigit()`
- Lists: creating lists and using `append()`
- Loops: `for` and `while`
- Conditions: `if`, `elif`, and `else`
- Built-in functions: `len()`, `sum()`, `max()`, `min()`, `sorted()`, and `any()`
- f-strings for formatted output
- `try` and `except` for handling invalid number input

## Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.

## How to Run

Open a terminal in this project folder.

Run the first program:

```bash
python result_card_generator.py
```

Run the second program:

```bash
python class_marks_analyzer.py
```

On some Windows computers, use `py` instead of `python`:

```bash
py result_card_generator.py
py class_marks_analyzer.py
```

## Sample Input and Output

### Program 1: Student Result Card Generator

Sample input:

```text
Enter student name:  ali ahmed
Enter roll number:  1025
Enter marks for English (0-100):  85
Enter marks for Mathematics (0-100):  90
Enter marks for Computer (0-100):  78
Enter marks for Physics (0-100):  80
Enter marks for Chemistry (0-100):  88
```

Sample output:

```text
STUDENT RESULT CARD
Student Name : Ali Ahmed
Roll Number  : 1025
English      : 85 / 100
Mathematics  : 90 / 100
Computer     : 78 / 100
Physics      : 80 / 100
Chemistry    : 88 / 100
Total Marks  : 421 / 500
Percentage   : 84.20%
Grade        : A
Final Status : Pass
```

### Program 2: Class Marks Analyzer

Sample input:

```text
How many students are in the class? 3

Student 1
Enter student name: Ali
Enter marks for Ali (0-100): 80

Student 2
Enter student name: Sara
Enter marks for Sara (0-100): 45

Student 3
Enter student name: Ahmed
Enter marks for Ahmed (0-100): 95
```

Sample output:

```text
CLASS MARKS REPORT
Number of Students : 3
Class Average      : 73.33
Passing Students   : 2
Failing Students   : 1

Highest Marks: 95
Student(s) with highest marks:
- Ahmed

Lowest Marks: 45
Student(s) with lowest marks:
- Sara

Students Above Class Average:
- Ali: 80
- Ahmed: 95

Marks from Highest to Lowest:
95
80
45
```

## GitHub Repository Structure

```text
python-functions-lists-assessment/
|
|-- result_card_generator.py
|-- class_marks_analyzer.py
|-- README.md
```

## Note

These programs are written in a simple style for learning and assessment practice. Run both programs and try different inputs, including invalid marks and roll numbers, before submitting.
