# https://programmers.co.kr/learn/courses/30/lessons/70128
# 프로그래머스 <내적>
# 월간 코드 챌린지 시즌1
a = [1,2,3,4]
b = [-3,-1,0,2]
"""def solution(a, b):
    answer = 0
    length = len(a)
    for i in range(length):
        answer += (a[i] * b[i])
    return answer"""
# zip 사용
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
print(solution(a, b))