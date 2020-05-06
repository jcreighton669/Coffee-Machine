student_score = float(input())
total_score = float(input())

grade_percentage = (student_score / total_score) * 100


if grade_percentage > 90.0:
    print("A")
elif grade_percentage > 80.0:
    print("B")
elif grade_percentage > 70.0:
    print("C")
elif grade_percentage > 60.0:
    print("D")
else:
    print("F")

