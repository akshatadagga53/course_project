import sys

print("=== Student Grade Calculator ===")

# Validate arguments
if len(sys.argv) != 4:
    print("Usage: python student_grade.py <Name> <Course> <Semester>")
    sys.exit(1)

name = sys.argv[1]
course = sys.argv[2]
semester = sys.argv[3]

print("Student Name:", name)
print("Course:", course)
print("Semester:", semester)

# Example grade logic
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

print("Marks:", marks)
print("Grade:", grade)
