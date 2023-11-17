# for 반복문
# randrange()
# from random import *
# print(randrange(1, 5))

# for waiting_num in range(1,6):
#     print("대기번호 : {0}".format(waiting_num))

# starbucks = ["아이언맨", "토르", "아이엠그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")