# https://leetcode.com/problems/minimum-path-sum/
import math

class Solution:
    def minPathSum(self, grid):
        r_len = len(grid)
        c_len = len(grid[0])
        
        memo = [[-1]*c_len for _ in range(r_len)]
        memo[0][0] = grid[0][0]

        def dfs(r,c):

            if r-1 >= 0 :
                if memo[r-1][c]!=-1:
                    up=memo[r-1][c]
                else:
                    up=dfs(r-1,c)
            else:
                up=math.inf

            if c-1 >=0 :
                if memo[r][c-1]!=-1:
                    right=memo[r][c-1]
                else:
                    right = dfs(r,c-1)
            else:
                right = math.inf

            cost = min(up,right)+grid[r][c]
            memo[r][c] = cost
            return cost

        if r_len == 1 and c_len ==1:
            return grid[0][0]
        answer = dfs(r_len-1, c_len-1)
        return answer

solution = Solution()
solution.minPathSum(grid = [[1,2,3],[4,5,6]])