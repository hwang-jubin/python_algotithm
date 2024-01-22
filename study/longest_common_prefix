# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs):
        answer = ""

        min_len = min(len(j) for j in strs)

        for i in range(min_len):
            char = strs[0][i]
            for j in range(1, len(strs)):
                new  = strs[j][i]
                if new != char:
                    return answer 
            answer+=char
        print(answer)
        return answer

solution = Solution()
print(solution.longestCommonPrefix(strs =
["flower","flow","flight"]))


