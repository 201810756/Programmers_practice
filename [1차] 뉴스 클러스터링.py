# https://programmers.co.kr/learn/courses/30/lessons/17677
# 프로그래머스 <[1차] 뉴스 클러스터링> level 2
# 2018 KAKAO blind recruitment
str1 = "E=M*C^2"
str2 = "e=m*c^2"
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    A, B = [], []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            A.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            B.append(str2[i:i+2])
    A_set = set(A)
    B_set = set(B)
    AndSet, OrSet = [], []
    for a in A_set&B_set:
        c = min(A.count(a),B.count(a))
        for i in range(c):
            AndSet.append(a)
    for o in A_set|B_set:
        c = max(A.count(o),B.count(o))
        for i in range(c):
            OrSet.append(o)
    if len(AndSet) == 0 and len(OrSet) == 0:
        answer = 65536
    else:
        answer = int((len(AndSet)/len(OrSet))*65536)
    return answer
print(solution(str1, str2))