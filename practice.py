# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

''' 한번에 여러개 주석처리 '''

print("우리집 "+animal+"의 이름은 "+name+"이에요")
hobby = "공놀이"
#print(name+"는 "+ str(age) +"살이며," +hobby+ "을 아주 좋아해요")
print(name, "는 ", age ,"살이며,", hobby, "을 아주 좋아해요")
print(name+"는 어른일까요? "+ str(is_adult))

print(10/3)
print(10//3)
print(10%3)

#abs 절대값
print(abs(-5))
#pow 제곱수
print(pow(4, 2))
#max 최대값
print(max(5, 12))
#min 최소값
print(max(5, 12))
#round 반올림
print(round(3.14))

from math import *
#floor 내림
print(floor(4.99))
#ceil 올림
print(ceil(3.14))
#sqrt 제곱근
print(sqrt(16))