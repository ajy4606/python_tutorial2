#자료구조의 변경

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

from random import *
users = range(1, 21) # 1부터 20까지 숫자 생성
users = list(users)

print(users)
shuffle(users)

winners = sample(users, 4)

print(winners)

print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))