# https://programmers.co.kr/learn/courses/30/lessons/62048
# 프로그래머스 <멀쩡한 사각형>
w = 8
h = 12
def solution(w, h):
    original_count = w*h
    delete_count = 0
    if w == h:
        delete_count = w
    elif h < w:
        delete_count = w*2
    else:
    answer = original_count - delete_count
    return answer
print(solution(w, h))