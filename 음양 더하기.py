# https://programmers.co.kr/learn/courses/30/lessons/76501
# 프로그래머스 <음양 더하기>
# 월간 코드 챌린지 시즌2
absolutes = [4,7,12]
signs = [True,False,True]
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
print(solution(absolutes, signs))