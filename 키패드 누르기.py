# https://programmers.co.kr/learn/courses/30/lessons/67256
# 프로그래머스 [키패드 누르기] Level 1
# 2020 KAKAO 인턴십
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
#numbers = [2]
hand = "left"
key_pad = [[1,2,3],
            [4,5,6],
            [7,8,9],
            ['*',0,'#']]
from collections import deque
def bfs(start,count,target):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = start
    queue = deque()
    queue.append((x,y,count))
    while queue:
        x, y, count = queue.popleft()
        if key_pad[x][y] == target:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<4 and 0<=ny<3:
                queue.append((nx,ny,count+1))
    return count
def solution(numbers, hand):
    answer = ''
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
    l_current = '*'
    r_current = '#'
    r_dis, l_dis = 0, 0
    for number in numbers:
        if number in left_key:
            answer += 'L'
            l_current = number
        elif number in right_key:
            answer += 'R'
            r_current = number
        else:
            for i in range(4):
                for j in range(3):
                    if key_pad[i][j] == r_current:
                        r_dis = bfs((i,j),0,number)
                    if key_pad[i][j] == l_current:
                        l_dis = bfs((i, j), 0, number)
            if r_dis == l_dis:
                if hand == "right":
                    answer += 'R'
                    r_current = number
                else:
                    answer += 'L'
                    l_current = number
            elif r_dis > l_dis:
                answer += 'L'
                l_current = number
            else:
                answer += 'R'
                r_current = number
    return answer

print(solution(numbers, hand))