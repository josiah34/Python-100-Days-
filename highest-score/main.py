student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for n in range(0, len(student_scores)):
    if student_scores[n] > highest_score:
        highest_score = student_scores[n]
        


print(f"The highest score in the class is: {highest_score}")



