student_scores = [88, 92, 75, 63, 100, 55, 81]
letter_grades = []

def assign_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    elif score < 60 and score >= 0:
        return "F"
    else:
        return "Invalid Score"
    
# Write 'and' instead of using '&'

for i in range(0, len(student_scores) - 1):
    grade = assign_grade(student_scores[i])
    letter_grades.append(grade)
    
# Okay so letter_grades.append[grade] was wrong because it requires () not [].
# len(student_scores[i]) would extend 1 longer then its corresponding list.

print("Student Scores:", student_scores)
print("Letter Grades:", letter_grades)

# Extra challenge:
# Count how many students got A or B using bitwise/logical operators
count_AB = 0
for grade in letter_grades:
    if grade == "A" or grade == "B":
        count_AB += 1
        
# Write 'or' not '|'.

print("Number of students who got A or B:", count_AB)