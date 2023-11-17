# 한 줄 for문
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# 택시 승객 손님
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51):
    time  = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1})분".format(i, time))
        cnt += 1
    else : 
        print("[ ] {0}번째 손님 (소요시간 : {1})분".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))