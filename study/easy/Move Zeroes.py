# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums) -> None:
        point = 0
        while point < len(nums):
            if nums[point] == 0:
                nums.remove(0)
                nums.append(0)
            point+=1

solution = Solution()
solution.moveZeroes(nums = [0])

# 0의 개수를 세고, 0이 아닌 것들을 앞으로 몰아서 넣고,
# 0의 개수만큼 뒤에 추가 하기
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        
        pos = 0
        for i in nums:
            if i != 0:
                nums[pos] = i
                pos += 1
        
        for i in range(len(nums) - count, len(nums)):
            nums[i] = 0
        