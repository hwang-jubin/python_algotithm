# https://leetcode.com/problems/missing-number/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        memo = set(nums)
        
        for i in range(len(nums)+1):
            if i not in memo:
                return i
        
solution = Solution()
solution.missingNumber(nums=[3,0,1])