#2019년 8월 5일 어느 오후
#추상화 def
#total과 avg를 만들어보자

scores= [10,20,30,40,50]

def total(scores):
    total_score= 0
    for i in range(len(scores)):
        total_score = scores[i] + total_score
    return total_score



print(total([10,20,30,40,50]))