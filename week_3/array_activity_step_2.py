#from array_list import Array2D
from array import Array2D

filename = "data.txt"

# Open the text file for reading.
grade_file = open( filename, "r" )

# Extract the first two values; indicate the size of the array.
num_students = int( grade_file.readline() )
num_exams = int( grade_file.readline() )

# Create the 2-D array to store the grades.
exam_grades = Array2D( num_students, num_exams )

# Extract the grades from the remaining lines.
i = 0
for student in grade_file :
  grades = student.split()

  for j in range( num_exams ):
    exam_grades[i,j] = int( grades[j] )
  i += 1

# Compute each student's average exam grade.
for i in range( num_students ) :

  total = 0
  for j in range( num_exams ) :
    total += exam_grades[i,j]

  exam_avg = total / num_exams
  print( f"{i+1:2}: {exam_avg:>6.2f}")

# Close the text file.
grade_file.close()
