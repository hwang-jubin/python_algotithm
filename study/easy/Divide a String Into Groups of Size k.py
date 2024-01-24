# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        string = ""
        for char in s:
            string+=char
            if len(string) == k:
                answer.append(string)
                string = ""

        if len(string) !=0:
            while len(string) !=k :
                string+=fill
            answer.append(string)

        return answer

solution = Solution()
solution.divideString(s = "abcdefghij", k = 3, fill = "x")