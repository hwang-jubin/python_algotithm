# DFS
from collections import deque

class Solution:

    def numIslands(self, grid) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False]*col_len for _ in range(row_len)]
        anwer = 0

        def check(r, c):
            return (r >= 0 and r < row_len) and (c >= 0 and c < col_len)

        def dfs(i, j):
            # 위, 오른쪽, 아래, 왼쪽
            r = [1,0,-1,0]
            c = [0,1,0,-1]
            
            visited[i][j] = True

            for num in range(4):
                next_r = i+r[num]
                next_c = j+c[num]
                if check(next_r,next_c):
                    if grid[next_r][next_c] == "1" and not visited[next_r][next_c]:
                        dfs(next_r, next_c)
            

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1" and visited[i][j]==False:
                    dfs(i,j,grid)
                    answer+=1
        return answer