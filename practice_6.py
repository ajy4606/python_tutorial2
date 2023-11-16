print("백문이 불여일견\n백견이 불여일타")

#저는 "나도 코딩" 입니다. (탈출문자)
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
print("E:\\coding_tutorial\\python_tutorial2")

# \r : 커서를 맨 앞으로 이동 (inset 형태로 자리를 대체)
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# url = "http://naver.com"
url = "http://youtube.com"
my_str = url.replace("http://","")
print(my_str)
point = my_str.find(".")
print(point)
print(my_str[my_str.find("."):])
my_str = my_str[:my_str.index(".")]
password = my_str[0:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))