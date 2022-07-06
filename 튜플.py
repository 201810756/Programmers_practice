# https://programmers.co.kr/learn/courses/30/lessons/64065
# 프로그래머스 <튜플> Level 2
# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{123}}"
def solution(s):
    answer = []
    splited_list = []
    split_s = s.split('},')
    for ss in split_s:
        for r in ['{','}']:
            ss = ss.replace(r,'')
        splited_list.append(ss)
    answer_list = []
    for num in splited_list :
        answer_list.append(list(map(int,num.split(','))))
    answer_list.sort(key = lambda x : len(x))
    for number in answer_list:
        for n in number:
            if n not in answer:
                answer.append(n)
            else:
                continue
    return answer
print(solution(s))