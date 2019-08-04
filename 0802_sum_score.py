scores = [80, 100, 70, 90, 40]

score=0

for i in range(0, 5):
    score = score + scores[i]
    print(i+1, '번째 누적 값 = ' ,score)


print('total score=' , score)





