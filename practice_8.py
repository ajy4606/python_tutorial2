cabinet = {3:"유재석", 100:"김태호"}  # key : value
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# cabinet에 없는 키값을 입력하면 오류와 함께 프로그램 종료

print(cabinet.get(5)) # None과 함께 프로그램 계속 실행
print(cabinet.get(5, "사용 가능")) 

print(3 in cabinet) # 자료가 있는지 없는지 확인 가능
print(5 in cabinet)

cabinet_2 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet_2["A-3"])

# 새 손님
print(cabinet_2)
cabinet_2["A-3"] = "김종국"
cabinet_2["C-20"] = "조세호"
print(cabinet_2)

# 간 손님
del cabinet_2["A-3"]
print(cabinet_2)

# Key들만 출력
print(cabinet_2.keys())
print(cabinet_2.values())
print(cabinet_2.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)