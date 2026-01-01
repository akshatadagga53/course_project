import sys

def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

def main():
    print("=== Student Grade Calculator ===")

    if len(sys.argv) != 4:
        print("Usage: python student_grade.py <Name> <Course> <Semester>")
        sys.exit(1)

    name = sys.argv[1]
    course = sys.argv[2]
    semester = sys.argv[3]

    print(name, course, semester)

# ✅ ONLY this runs main
if __name__ == "__main__":
    main()
