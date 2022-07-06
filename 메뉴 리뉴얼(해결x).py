# https://programmers.co.kr/learn/courses/30/lessons/72411
# 프로그래머스 <메뉴 리뉴얼> Level 2
# 2021 KAKAO blind recruitment
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
from itertools import combinations as cb
def solution(orders, course):
    answer = []
    for num in course:
        counts = []
        max_count = 2
        for i in range(len(orders)):
            if len(orders[i]) >= num:
                for tup in cb(orders[i], num):
                    count = 1
                    for j in range(len(orders)):
                        if j != i:
                            if len(orders[j]) >= num:
                                for tup_2 in cb(orders[j], num):
                                    if tup == tup_2:
                                        count += 1
                    if count > max_count:
                        counts.clear()
                        counts.append(tup)
                        max_count = count
                    elif count == max_count:
                        if tup not in counts:
                            counts.append(tup)
        for k in counts:
            tmp = ''
            for j in k:
                tmp += j
            answer.append(tmp)
        answer.sort()
    return answer
print(solution(orders, course))