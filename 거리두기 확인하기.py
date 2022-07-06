# https://programmers.co.kr/learn/courses/30/lessons/81302
# 프로그래머스 <거리두기 확인하기> level 2
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
from collections import deque
def check(board, start_x, start_y):
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * 5 for _ in range(5)]
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True
    while queue:
        x, y, dis = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and board[nx][ny] != 'X':
                if board[nx][ny] == 'P':
                    if dis+1 <= 2:
                        return False
                    else:
                        visited[nx][ny] = True
                        queue.append((nx,ny,0))
                else:
                    visited[nx][ny] = True
                    queue.append((nx,ny,dis+1))
    return True
def solution(places):
    answer = []
    for place in places:
        board = []
        for seat in place:
            board.append(list(seat))
        flag = 0
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'P':
                    if check(board, i, j):
                        continue
                    else:
                        flag = 1
                        break
            if flag == 1:
                break
        if flag == 1:
            answer.append(0)
        else:
            answer.append(1)
    return answer
print(solution(places))