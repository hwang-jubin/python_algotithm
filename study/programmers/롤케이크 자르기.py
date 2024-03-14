# https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):
    answer = 0
    memo = {}
    for i in range(len(topping)):
        if topping[i] not in memo:
            memo[topping[i]] = 1
        else:
            memo[topping[i]]+=1

    old = set()
    for i in range(len(topping)):
        old.add(topping[i])
        memo[topping[i]]-=1
        if memo[topping[i]] == 0:
            memo.pop(topping[i])
        
        if len(memo) == len(old):
            answer+=1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))