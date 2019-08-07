class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

total_score = 0
count_student = 0


for class_score in class_scores:
    for score in class_score:
        total_score  = total_score + score
        print(total_score)

print('최종 합:', total_score)

for i in range(3):
   count_student = count_student + len(class_scores[i])
   print(i,'번째:', count_student)

avg_score = total_score/count_student
print('평균은', avg_score ,'입니다!')
