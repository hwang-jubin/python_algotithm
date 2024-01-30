class Solution:
    def singleNumber(self, nums) -> int:
        memo = {}
        for i in nums:
            if i not in memo:
                memo[i] = 1
            else:
                memo[i]+=1

        for i in memo:
            if memo[i] == 1:
                return i
            
solution = Solution()
solution.singleNumber(nums = [4,1,2,1,2])