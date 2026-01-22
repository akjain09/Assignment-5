student_marks = {
    "Amit": 85,
    "Neha": 90,
    "Rahul": 78,
    "Priya": 88,
    "Suman": 92
}

name = input("Enter the student's name: ")


if name in student_marks:
    print(f"{name}'s Marks:{student_marks[name]}")
else:
    print("Student not found.")
