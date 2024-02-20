# https://leetcode.com/problems/non-decreasing-subsequences/

class Solution:
    def findSubsequences(self, nums):
        answer = set()
        def recur(i, arr):

            for next in range(i+1,len(nums)):
                if nums[next] >= nums[i]:
                    c_array = arr.copy()
                    c_array.append(nums[next])
                    answer.add(tuple(c_array))
                    
                    recur(next,c_array)

        for i in range(len(nums)-1):
            arr = []
            arr.append(nums[i])
            recur(i,arr)
        
        return list(answer)
    
solution = Solution()
solution.findSubsequences(nums = [4,6,7,7])