scores = [80, 100, 70, 90, 40]

score=0

for i in range(0, len(scores)):      #len(scores)=5니까
    score = score + scores[i]
    print(i+1, '번째 누적 값 = ' ,score)


print('total score=' , score)





