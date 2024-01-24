# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0 
        right = len(s)-1
        while left<right and s[left] == s[right]:
            same = s[left]
            while left <= right and s[left] == same :
                left +=1
                if left == len(s):
                    return 0
            while left <= right and s[right] == same:
                right -=1
                
        return right - left + 1
solution = Solution()
print(solution.minimumLength(s = "aaa"))

# Input: s = "aabccabba"