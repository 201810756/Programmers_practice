# https://programmers.co.kr/learn/courses/30/lessons/86051
# 프로그래머스 <없는 숫자 더하기>
# 월간 코드 챌린지 시즌3
numbers = [1,2,3,4,6,7,8,0]
def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer
print(solution(numbers))