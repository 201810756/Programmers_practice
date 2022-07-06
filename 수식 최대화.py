# https://programmers.co.kr/learn/courses/30/lessons/67257
# 프로그래머스 <수식 최대화> Level 2

expression = "50*6-3*2"
import itertools
def solution(expression):
    answer = 0
    instruction = ['*', '+', '-']
    exist_inst = []
    new_list = []
    tmp = ''
    for i in range(len(expression)):
        if expression[i] in instruction:
            new_list.append(int(tmp))
            new_list.append(expression[i])
            tmp = ''
            if expression[i] not in exist_inst:
                exist_inst.append(expression[i])
            else:
                continue
        else:
            tmp += expression[i]
            if i == len(expression)-1:
                new_list.append(int(tmp))
    max_value = 0
    for i in itertools.permutations(exist_inst,len(exist_inst)):
        sample_list = new_list
        for k in i:
            while k in sample_list:
                index = sample_list.index(k)
                if k == '-':
                    tmp = sample_list[index-1]-sample_list[index+1]
                elif k == '+':
                    tmp = sample_list[index-1]+sample_list[index+1]
                else:
                    tmp = sample_list[index-1]*sample_list[index+1]
                sample_list = sample_list[:index-1]+[tmp]+sample_list[index+2:]
        tmp_value = sample_list[-1]
        max_value = max(max_value, abs(tmp_value))
    return max_value
print(solution(expression))