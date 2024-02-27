# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# 최단거리 찾을 때는 BFS 사용하면 좋음
# DFS
import sys
def solution(maps):
    answer = sys.maxsize
    rl = len(maps)
    cl = len(maps[0])
    memo = [[False]*cl for _ in range(rl)]
    
    def dfs(r,c,sum):
        nonlocal rl
        nonlocal cl
        nonlocal answer
        if r == rl-1 and c == cl-1:
            answer = min(answer, sum)

        dir = [(-1,0),(0,1),(1,0),(0,-1)]
        
        for dr, dc in dir:
            row = r+dr
            col = c+dc
            if 0<=row<rl and 0<=col<cl:
                if memo[row][col]==False and maps[row][col] == 1:
                    memo[row][col] = True
                    dfs(row, col, sum+1)
                    memo[row][col] = False

    memo[0][0] = True
    dfs(0,0,1)
    if answer == sys.maxsize:
        return -1
    else:
        return answer
    
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))



# BFS
from collections import deque

def solution(maps):

    rl = len(maps)
    cl = len(maps[0])
    memo = [[False]*cl for _ in range(rl)]

    q = deque()

    dir = [(-1,0),(0,1),(1,0),(0,-1)]

    q.append((0,0,1))

    while q :
        r,c,sum = q.popleft()
        if r == rl-1 and c == cl-1:
            return sum

        for dr, dc in dir:
            row = r+dr
            col = c+dc
            if 0<=row<rl and 0<=col<cl:
                if memo[row][col]==False and maps[row][col] == 1:
                    q.append((row,col,sum+1))
                    memo[row][col] = True


    return -1