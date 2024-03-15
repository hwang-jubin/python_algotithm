from collections import deque
def solution(n):
    q = deque()
    answer = ""
    while n >= 3:
        r = n%3
        n = n//3
    
        if r == 0:
            q.append('4')
            n = n-1
        elif r == 1:
            q.append('1')
        elif r == 2:
            q.append('2')
    if n !=0:
        q.append(str(n))
    while q:
        answer+=q.pop()

    return str(answer)