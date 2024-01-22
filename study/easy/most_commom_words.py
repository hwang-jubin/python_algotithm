# https://leetcode.com/problems/most-common-word/description/

from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banneds = set()

        for ban in banned:
            banneds.add(ban)

        memo = {}
        memo_str = ""
        for char in paragraph:
            if 65<=ord(char)<=122:
                memo_str+=char.lower()
            elif memo_str:
                if memo_str not in memo and memo_str not in banneds :
                    memo[memo_str] = 1
                elif memo_str in memo:
                    memo[memo_str] +=1
                memo_str = ""

        if memo_str:
            if memo_str not in memo and memo_str not in banneds :
                memo[memo_str] = 1
            elif memo_str in memo:
                memo[memo_str] +=1

        max_value = max(memo , key = memo.get)
        return max_value

solution = Solution()
print(solution.mostCommonWord(paragraph ="Bob", banned =[]))
