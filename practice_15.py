#continue break

absent = [2, 5] # 결석
no_book = [7]

for student in range(1, 11): 
    if student in absent:
        continue
    if student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 익어봐".format(student))