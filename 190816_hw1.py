
#A,B,C,D,E 성적 산출하기

grade = 0

while  grade  != -1 :
      grade = int(input('성적을 입력하세요'))


      if grade >= 80 :
            print ('축하합니다! A 입니다.')

      elif grade >= 60 :
            print('B입니다.')

      elif grade >= 40 :
            print('C 입니다.')

      elif grade > 20 :
            print('D 입니다.')

      else:
            print('큰일났어요! F 입니다.')

