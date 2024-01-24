# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/?envType=daily-question&envId=2024-01-23

from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s) == len(set(s))

        def backtrack(start, current):
            nonlocal max_length
            # 현재까지의 문자열이 유니크하면 최대 길이 갱신
            if is_unique(current):
                max_length = max(max_length, len(current))

            # 각 문자열을 현재 문자열에 추가하면서 재귀 호출
            for i in range(start, len(arr)):
                backtrack(i + 1, current + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length
                

solution = Solution()
print(solution.maxLength(arr = ["crd","s","crdt"]))
