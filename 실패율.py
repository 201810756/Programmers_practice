# https://programmers.co.kr/learn/courses/30/lessons/42889
# 프로그래머스 <실패율>
# 2019 KAKAO blind recruitment
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# 실패율 :
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
def solution(N, stages):
    num_player = len(stages)
    order = []
    for i in range(1,N+1):
        tmp = stages.count(i)
        if tmp == 0:
            order.append((i,0))
        else:
            order.append((i,tmp/num_player))
        num_player -= tmp
    order.sort(key = lambda x : x[1], reverse=True)
    answer = [order[i][0] for i in range(len(order))]
    return answer
# dictionary 사용
"""def solution(N, stages):
    order = {}
    num_player = len(stages)
    for i in range(1, N+1):
        tmp = stages.count(i)
        if tmp == 0:
            order[i] = 0
        else:
            order[i] = tmp/num_player
        num_player -= tmp
    return sorted(order, key = lambda x : order[x], reverse=True)"""
print(solution(N, stages))