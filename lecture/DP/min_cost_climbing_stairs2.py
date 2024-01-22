# bottom-up
# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        memo = [-1]*(len(cost)+1)

        memo[0] = 0
        memo[1] = 0

        for i in range(2, len(cost)+1):
            
            memo[i] = min(memo[i-1]+cost[i-1],memo[i-2]+cost[i-2])

        return memo[len(cost)]
    

solution = Solution()
solution.minCostClimbingStairs(cost=[10,15,20])