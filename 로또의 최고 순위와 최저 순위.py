# https://programmers.co.kr/learn/courses/30/lessons/77484
# 프로그래머스 <로또 최고 순위와 최저 순위>
lottos = [45, 4, 35, 20, 3, 9]
win_nums = 	[20, 9, 3, 45, 4, 35]
def solution(lottos, win_nums):
    best_count, worst_count, zero_count = 0, 0, 0
    order = [0,6,5,4,3,2,0]
    answer = []
    for lotto in lottos:
        if lotto != 0:
            if lotto in win_nums:
                best_count += 1
                worst_count += 1
        else:
            zero_count += 1
    best_count += zero_count
    if best_count != 0 and best_count != 1:
        answer.append(order.index(best_count))
    else:
        answer.append(6)
    if worst_count != 0 and worst_count != 1:
        answer.append(order.index(worst_count))
    else:
        answer.append(6)
    return answer
# 다른 사람의 풀이
"""def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_zero = lottos.count(0)
    count = 0
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
    return rank[count + cnt_zero], rank[count]"""
print(solution(lottos, win_nums))