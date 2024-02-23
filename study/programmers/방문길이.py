# https://school.programmers.co.kr/learn/courses/30/lessons/49994?language=python3

def solution(dirs):
    answer = 0 
    memo = {}
    x = 0
    y = 0
    memo[(0,0)] = []
    for c in dirs:
        bool = True
        nx = x
        ny = y
        if c == 'U':
            ny = y+1
        elif c == 'D':
            ny = y-1
        elif c == 'L':
            nx = x-1
        elif c == 'R':
            nx = x+1

        if -5 > nx or nx > 5 or ny < -5 or ny > 5:
            continue

        for (a,b) in memo[(x,y)]:
            if a == nx and b == ny:
                bool = False
                break
        
        if bool:
            answer += 1
            memo[(x,y)].append((nx,ny))
            if (nx,ny) not in memo:
                memo[(nx,ny)] = [(x,y)]
            else:
                memo[(nx,ny)].append((x,y))

        x = nx
        y = ny
    
    return answer


print(solution("LULLLLLLU"))