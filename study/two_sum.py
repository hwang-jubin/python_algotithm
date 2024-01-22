from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        answer = []
        index = 0

        for i in range(len(nums)):
            num = target-nums[i]
            if num in memo:
                answer.append(memo[num])
                answer.append(i)
                return answer
            memo[nums[i]] = i
    
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
