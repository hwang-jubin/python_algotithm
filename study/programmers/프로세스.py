from collections import deque

def solution(priorities, location):
    answer = 0

    q = deque()
    for index,priority in enumerate(priorities):
        q.append((priority,index))

    num = 0
    while q:
        f,i = q.popleft()
        biggest = True
        for p in priorities:
            if f < p:
                biggest = False
                break

        if biggest:
            priorities[i] = 0
            num+=1
            if i == location:
                return num
        else:
            q.append((f,i))

print(solution([2, 1, 3, 2],2))
