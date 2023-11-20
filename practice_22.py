print("Python", "Java", "JavaScript", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("Pyton", "Java", file=sys.stdout) # 표준 출력으로
print("Pyton", "Java", file=sys.stderr) # 표준 에러 처리

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    #ljust(8) 왼쪽 정렬 8칸의 공간을 확보한 상태에서

# 은행 대기순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
# input 사용자 입력으로 받았을 때는 항상 string으로 받음
print("입력하신 값은 " + answer + "입니다.")