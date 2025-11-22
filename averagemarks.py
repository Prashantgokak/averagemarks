import sys
if len(sys.argv) != 6:
  print("Usage: python student.py <sub1> <sub2> <sub3> <sub4> <sub5>")
  sys.exit(1)
sub1 = int(sys.argv[1])
sub2 = int(sys.argv[2])
sub3 = int(sys.argv[3])
sub4 = int(sys.argv[4])
sub5 = int(sys.argv[5])
avgMarks = (sub1 + sub2 + sub3 + sub4 + sub5)/ 5
grade = "null"
if avgMarks >= 90 :
  grade = "A"
elif avgMarks >= 80:
  grade = "B"
elif avgMarks >= 70:
  grade = "C"
elif avgMarks >= 40:
  grade = "D"
elif avgMarks < 40:
  grade = "Fail"
else:
  print("invalid")

print("Average marks: ", avgMarks)
print("Grade: ", grade)
