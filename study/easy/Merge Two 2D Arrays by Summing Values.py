# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/
from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        memo = {}
        for num in nums1:
            if  num[0] not in memo:
                memo[num[0]] = num[1]
            else:
                memo[num[0]] += num[1]

        for num in nums2:
            if  num[0] not in memo:
                memo[num[0]] = num[1]
            else:
                memo[num[0]] += num[1]
        

        answer = [[key, value] for key, value in sorted(memo.items())]

        return answer
    

solution = Solution()
print(solution.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))



# Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
# Output: [[1,6],[2,3],[3,2],[4,6]]