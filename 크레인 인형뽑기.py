# https://programmers.co.kr/learn/courses/30/lessons/64061
# 프로그래머스 <크레인 인형뽑기> Level 1
# 2019 KAKAO 겨울 인턴십
board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
def solution(board, moves):
    answer = 0
    box = []
    for move in moves:
        for i in range(len(board)):
            flag = 0
            if board[i][move-1] != 0:
                flag = 1
                number = board[i][move-1]
                if len(box) != 0:
                    if number == box[-1]:
                        answer += 2
                        box.pop()
                    else:
                        box.append(number)
                else:
                    box.append(number)
                board[i][move-1] = 0
                if flag == 1:
                    break
    return answer


print(solution(board, moves))