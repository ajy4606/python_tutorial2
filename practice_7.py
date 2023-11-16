# 리스트 []

# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10,20,30]

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))

subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
subway.pop()
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용
num_list = [5,4,3,2,1]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list)