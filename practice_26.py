# import pickle

# with open("profile.pickle", "rb") as profile_file: #profile_file이란 변수에 담음
#     print(pickle.load(profile_file))
# #close를 따로 할 필요가 없음

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요~")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())