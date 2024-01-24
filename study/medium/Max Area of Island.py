from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r_len = len(grid)
        c_len = len(grid[0])
        memo = [[False]*c_len for _ in range(r_len)]
        max_len = 0
        sum = 0
        def dp(r, c):
            nonlocal max_len
            nonlocal r_len
            nonlocal c_len
            nonlocal sum
            # 위부터 시계방향
            r_dir = [-1,0,1,0]
            c_dir = [0,1,0,-1]
            
            memo[r][c] = True
            sum +=1

            for i in range(len(r_dir)):
                row = r+r_dir[i]
                col = c+c_dir[i]
                if 0<=row<r_len and 0<=col<c_len:
                    if grid[row][col] == 1 and memo[row][col] is False:
                        dp(row, col)

        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == 1 and memo[i][j] == False:
                    dp(i,j)
                    max_len = max(max_len , sum)
                    sum = 0
        return max_len
    
solution = Solution()
solution.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])