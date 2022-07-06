# https://programmers.co.kr/learn/courses/30/lessons/72412
# 프로그래머스 <순위 검색> Level 2
# 2021 KAKAO blind recruitment
info = ["java backend junior pizza 150","python frontend senior chicken 210",
        "python frontend senior chicken 150","cpp backend senior pizza 260",
        "java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250","- and backend and senior and - 150",
         "- and - and - and chicken 100","- and - and - and - 150"]
def solution(info,query):
    answer = []
    info_list = []
    query_list = []
    for i in info:
        n = i.replace('and', '')
        n = n.split()
        info_list.append(n)
    for q in query:
        n = q.replace('and','')
        n  = n.split()
        query_list.append(n)
    for q in query_list:
        hubo = info
        for i in range(len(q)):
            if q[i] == '-':
                continue
            else:
                for j in range(len(hubo)):
                    if hubo[j][i] == q[i]:

    return answer
print(solution(info, query))