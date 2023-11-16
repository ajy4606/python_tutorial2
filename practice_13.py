# for 반복문
# randrange()
from random import *
print(randrange(1, 5))

for waiting_num in range(1,6):
    print("대기번호 : {0}".format(waiting_num))

starbucks = ["아이언맨", "토르", "아이엠그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))