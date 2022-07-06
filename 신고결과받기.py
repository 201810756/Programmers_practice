# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
# 프로그래머스 [신고 결과 받기] Level 1
# 2022 KAKAO BLIND Recruitment
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
"""id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3"""
# k번 이상 신고된 유저 -> 정지
# 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return
# id_list = ID가 담긴 문자열 배열
# report = 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    warn = {}
    for l in report:
        warn_from, warn_to = l.split()
        if warn_to not in warn:
            warn[warn_to] = [1, warn_from]
        else:
            if warn_from not in warn[warn_to]:
                warn[warn_to][0] += 1
                warn[warn_to].append(warn_from)
            else:
                continue
    for key,value in warn.items():
        if value[0] >= k:
            for f in value[1:]:
                answer[id_list.index(f)] += 1
    return answer
print(solution(id_list, report, k))

"""
참고 풀이 
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
"""