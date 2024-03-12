# https://school.programmers.co.kr/learn/courses/30/lessons/12924?language=python3

def solution(n):
    answer = 0

    def sum(i):
        nonlocal answer
        s = i
        while i>0:
            next = s+i-1
            if next == n:
                answer +=1
                return
            elif n-next < i-2:
                return
            else:
                s=next
            i = i-1


    start = 0
    if n%2!=0:
        start=(n//2)+1
    else:
        start= n//2

    for i in range(start,1,-1):
        sum(i)

    return answer+1

print(solution(1))