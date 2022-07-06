# https://programmers.co.kr/learn/courses/30/lessons/60058
# 프로그래머스 <괄호 변환> Level 2
# 2020 KAKAO blind recruitment
"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 
더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""
p = ")("
def check_complete(s):
    check = []
    for chr in s:
        if len(check) >= 1:
            if chr == ')' and check[-1] == '(':
                check.pop()
            else:
                check.append(chr)
        else:
            check.append(chr)
    if len(check) == 0:
        return True
    else:
        return False
def sol_func(tmp):
    u = ''
    v = ''
    if len(tmp) == 0:
        return ''
    else:
        for i in range(len(tmp)):
            sample = tmp[:i + 1]
            if sample.count('(') == sample.count(')'):
                u = tmp[:i + 1]
                v = tmp[i + 1:]
                break
        if check_complete(u):
            return u+sol_func(v)
        else:
            sample = '('+sol_func(v)+')'
            u = u[1:-1]
            update_u  = ''
            for i in range(len(u)):
                if u[i] == '(':
                   update_u += ')'
                else:
                    update_u += '('
            return sample+update_u
def solution(p):
    if check_complete(p):
        answer = p
    else:
        answer = sol_func(p)
    return answer
print(solution(p))