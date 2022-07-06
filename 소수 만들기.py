# https://programmers.co.kr/learn/courses/30/lessons/12977
# 프로그래머스 <소수 만들기>
nums = [1,2,7,6,4]
"""def prime_check(number):
    flag = 0
    for i in range(2, number):
        if number % i == 0:
            flag = 1
            break
    if flag == 1:
        return False
    else:
        return True"""
# 에라토스테네스의 체 활용하기
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for  i in range(2,n) if sieve[i]]
def solution(nums):
    answer = 0
    tmp = 0
    prime = prime_list(3000)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) in prime:
                    answer +=1 
    return answer
print(solution(nums))


"""for i in range(len(nums)-2):
        tmp += nums[i]
        for j in range(i+1, len(nums)-1):
            tmp += nums[j]
            for k in range(j+1, len(nums)):
                tmp += nums[k]
                if prime_check(tmp):
                    tmp -= nums[k]
                    answer += 1
                else:
                    tmp -= nums[k]
            tmp -= nums[j]
        tmp -= nums[i]"""