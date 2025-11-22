import sys

# Expect exactly 5 subject marks
if len(sys.argv) != 6:
    print("Usage: python student.py <sub1> <sub2> <sub3> <sub4> <sub5>")
    sys.exit(1)

try:
    # Convert inputs to integers
    marks = [int(arg) for arg in sys.argv[1:6]]
except ValueError:
    print("Error: All subject marks must be integers.")
    sys.exit(1)

# Calculate average
avgMarks = sum(marks) / 5

# Determine grade
if avgMarks >= 90:
    grade = "A"
elif avgMarks >= 80:
    grade = "B"
elif avgMarks >= 70:
    grade = "C"
elif avgMarks >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"Average marks: {avgMarks:.2f}")
print(f"Grade: {grade}")
