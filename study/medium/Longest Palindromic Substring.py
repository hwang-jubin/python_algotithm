# https://leetcode.com/problems/longest-palindromic-substring/submissions/1161676721/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        def dfs(st):
            nonlocal answer 
            length = len(st)
            if length == 1:
                if len(answer) < length:
                    answer = st
                return
            pal = True
            for i in range(length//2):
                if st[i] !=st[length-i-1]:
                    pal = False
                    break
            if pal:
                if len(answer) < length:
                    answer = st
                return answer
            else:
                string = st[0:length-1]
                dfs(string)
        
        for i in range(len(s)):
            string = s[i:]
            if dfs(string):
                return answer
        return answer

solution = Solution()
print(solution.longestPalindrome(s = "aacabdkacaa"))

# Input: s = "cbbd"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        len_res = 0
        for i in range(len(s)):
            r, l = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len_res:
                    result = s[l:r+1]
                    len_res = r - l + 1
                l -= 1
                r += 1       
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len_res:
                    result = s[l:r+1]
                    len_res = r - l + 1
                l -= 1
                r += 1
        return result

            