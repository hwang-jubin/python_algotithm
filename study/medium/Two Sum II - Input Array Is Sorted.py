# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    # hash map 으로 구현
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        answer = []
        for index in range(len(numbers)):
            num = numbers[index]
            minus = target - num
            if minus in memo:
                answer.append(memo[minus])
                answer.append(memo[index+1])
                return answer
            else:
                memo[num] = index+1
            
    # 이진탐색
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0 
        right = len(numbers)-1
        while left <=right:
            sum = numbers[left]+numbers[right]
            if target > sum:
                left += 1
            elif target < sum:
                right -= 1
            elif target == sum:
                return [left+1, right+1]

