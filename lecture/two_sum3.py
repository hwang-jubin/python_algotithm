
class Solution:
    def twosum(self, nums, target):
        memo = {}
    
        for p in nums:
            if target - p in memo:
                return True
            memo[p]=1
        return False

solution_instance = Solution()
print(solution_instance.twosum(nums=[3,1,5,6], target = 8))