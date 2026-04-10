student_score = [100, 99, 67, 49, 93, 67, 98, 45, 56, 76, 89, 91, 78, 79, 95, 57, 43, 10, 89, 95, 83]
# highest_score = max(student_score)
# print(highest_score)

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score

print(highest_score)