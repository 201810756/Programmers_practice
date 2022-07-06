# https://programmers.co.kr/learn/courses/30/lessons/72410
# 프로그래머스 [신규 아이디 추천] Level 1
# 2021 KAKAO BLIND Recruitment
new_id = "...!@BaT#*..y.abcdefghijklm"
# ID 규칙 : 3자 이상 15자 이하
# 소문자, 숫자, -, _, .만 쓸 수 있음
# .은 처음과 끝에 사용할 수 없으며 연속으로 사용 불가능

def solution(new_id):
    answer = ''
    # 1단계
    answer = new_id.lower()
    # 2단계
    have_to_remove = "~!@#$%^&*()=+[{]}:?,<>/"
    for c in have_to_remove:
        if c in answer:
            answer = answer.replace(c,'')
    # 3단계
    point_set = []
    index = 0
    while index < len(answer):
        count = 0
        if answer[index] == '.':
            for i in range(index+1, len(answer)):
                if answer[i] != '.':
                    break
                else:
                    count += 1
            if count >= 1:
                point_set.append('.'*(count+1))
        # index += (count+1)
        index += 1
    for point in point_set:
        answer = answer.replace(point,'.')
    # 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer
print(solution("a...a"))



