# top down
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1]*(n+1)

        def top_down(n):
            if n == 1 or n == 0:
                return 1
            
            if memo[n] == -1:
                memo[n] = top_down(n-1)+top_down(n-2)

            return memo[n]
        return top_down(n) 