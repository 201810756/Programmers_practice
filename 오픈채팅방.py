# https://programmers.co.kr/learn/courses/30/lessons/42888
# 프로그래머스 <오픈채팅방> Level 2
# 2019 KAKAO blind recruitment
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
          "Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    answer = []
    name_dict = {}
    for log in record:
        logs = log.split()
        if logs[0] == "Enter" or logs[0] == "Change":
            name_dict[logs[1]] = logs[2]
    for log in record:
        logs = log.split()
        if logs[0] == "Enter":
            answer.append(name_dict[logs[1]]+"님이 들어왔습니다.")
        elif logs[0] == "Leave":
            answer.append(name_dict[logs[1]]+"님이 나갔습니다.")
    return answer
print(solution(record))