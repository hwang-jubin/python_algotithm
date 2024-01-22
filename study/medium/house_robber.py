

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        memo = {}
        if length <=0:
            return 0

        memo[0] = nums[0]
        memo[1] = nums[1]

        

        def dp(n):
            # 2일 때 0과 -1을 비교할 수 없어서 그냥 -1은 0을 반환
            if n<0:
                return 0
            
            if n not in memo:
                memo[n] = max(dp(n-2), dp(n-3))+nums[n]
            return memo[n]

        answer = max(dp(length-1), dp(length-2))
        return answer
    
solution = Solution()
solution.rob(nums = [0])