# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
scores_in_each_subjects={
    "Net Centric Computing": 58,
    "E-commerce": 55,
    "E-governance" :59,
    "Compiler": 58,
    "Technical Wrting": 55,
    "Software Engineering": 57,
}
#print(len(scores_in_each_subjects))
# total_obtained_score=0
# for i in scores_in_each_subjects:
#     total_obtained_score +=scores_in_each_subjects[i]
total_obtained_score = sum(scores_in_each_subjects.values())

#here 60 denotes that each subject is of 60 full marks
full_marks_per_subject = 60
total_full_marks = full_marks_per_subject * len(scores_in_each_subjects)
percentage_score = (total_obtained_score / total_full_marks) * 100
# print(percentage_score)

if 90<= percentage_score <= 100:
    grade="A"
elif 80<= percentage_score<=89:
     grade="B"
elif 70<= percentage_score<=79:
     grade="C"
elif 60<= percentage_score<=69:
     grade="D"
else:
    grade="F"

print(f"Your percentage is {percentage_score:.2f}%.Your Grade is {grade}. ")

