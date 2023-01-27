student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
total_height = 0
# Loop through the list of heights and add them to total_height
for height in student_heights:
    total_height += height

#Find the total number of students by using the len() function
number_of_students = len(student_heights)

# Divide the total height by the total number of students to get the average height
average_height = round(total_height / number_of_students)

# Print the average height
print(average_height)