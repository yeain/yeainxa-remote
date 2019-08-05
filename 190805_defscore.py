#2019년 8월 5일 어느 오후
#추상화 def
#total과 avg를 만들어보자

scores= [10,20,30,40,50]

def total(x):
    return sum(x)

print(total(scores))


def avg(y):
    return sum(y)/len(y)

print(avg(scores))
