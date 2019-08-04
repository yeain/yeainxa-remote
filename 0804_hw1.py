class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

total_score =0


for class_score in class_scores:
    for score in class_score:
        total_score  = total_score + score
        print(total_score)

print('최종 합:', total_score)


# for class_score in class_scores:
#     total score = score+class_scores[i]
#     print(total_score)

