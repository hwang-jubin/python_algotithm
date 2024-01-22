# https://leetcode.com/problems/majority-element/
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = {}

        for key in nums:
            if key not in memo:
                memo[key] = 1
            else:
                memo[key] +=1
        
        max_key= max(memo ,key = memo.get)
        if len(nums)/2<=memo[max_key]:
            return max_key