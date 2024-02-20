# https://leetcode.com/problems/target-sum/submissions/1180577823/

class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        memo = {}
        
        def dfs(i, sum):
            if (i,sum) in memo:
                return memo[(i,sum)]

            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0
            else:
                plus = dfs(i+1, sum+nums[i])
                minus = dfs(i+1, sum-nums[i])

            memo[(i, sum)] = plus+minus
            return memo[(i,sum)]

        # 초기 호출을 수행합니다.
        return dfs(0, 0)


solution = Solution()
print(solution.findTargetSumWays(nums=[1,1,1,1,1], target=3))