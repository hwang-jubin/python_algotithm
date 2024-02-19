# https://leetcode.com/problems/longest-string-chain/?envType=daily-question&envId=2024-01-20
import collections

# bottom up
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 단어를 길이순으로 정렬
        words.sort(key=len)
        # 각 단어의 최대 체인 길이를 저장할 딕셔너리
        dp = {}
        max_chain_length = 1
        
        for word in words:
            # 현재 단어의 최대 체인 길이를 1로 초기화
            dp[word] = 1
            # 단어에서 한 글자씩 뺀 모든 가능한 단어들을 탐색
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                # 만약 해당 단어가 이전에 등장한 단어라면 체인을 업데이트
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            max_chain_length = max(max_chain_length, dp[word])
        
        return max_chain_length


solution = Solution()
solution.longestStrChain(words = ["a","b","ba","bca","bda","bdca"])



# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

