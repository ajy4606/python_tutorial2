python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 대문자인지
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
print(python.index("n", 6))

print(python.find("n"))
print(python.find("Java"))
#print(python.index("Java"))

print(python.count("n"))