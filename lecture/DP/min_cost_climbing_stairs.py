# top-down

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        memo = [-1]*(len(cost)+1)

        def td(n):
            if n==0 or n==1:
                return 0

            if memo[n]==-1:
                memo[n] = min(td(n-1)+cost[n-1], td(n-2)+cost[n-2])

            return memo[n]
            
        return td(len(cost))
    

solution = Solution()
solution.minCostClimbingStairs(cost=[10,15,20])