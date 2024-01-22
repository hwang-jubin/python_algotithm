# https://leetcode.com/problems/unique-paths/description/
# top bottom

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1]*n for _ in range(m)]

        def dp(r,c):
            if r == 0 and c == 0:
                memo[r][c] = 1
                return 1
            
            path = 0
            if memo[r,c] == - 1:
                if r-1 >=0 :
                    path += dp(r-1,c)
                if c-1 >=0 :
                    path +=dp(r, c-1)

                memo[r,c] = path

            return memo[r, c]
        
        return dp(m-1,n-1)