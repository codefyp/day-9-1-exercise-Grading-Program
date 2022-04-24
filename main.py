student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    #create a score variable which equals each student_scores key
    score = student_scores [student]
    #run an if to add the grade scores
    if score > 90 :
        student_grades [student] = "Outstadnding"
    elif score > 80 :
        student_grades [student] = "Exceeds Expectations"
    elif score > 70 :
        student_grades [student] = "Acceptable"
    else:
        student_grades [student] = "Fail"   
    
#students_grades = {student_scores[k]: v for k, v in students_grades[k]} 
    

# 🚨 Don't change the code below 👇
print(student_grades)
