from student_grade import calculate_average, assign_grade

def test_average():
    assert calculate_average([70, 80, 90]) == 80

def test_grade_A():
    assert assign_grade(95) == "A"

def test_grade_C():
    assert assign_grade(65) == "C"
