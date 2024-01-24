# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        memo = {}
        answer = 0
        same = set()
        for word in words:
            # dictionary 에 list 에 있는 값을 넣기
            if word in memo:
                    memo[word] +=1
            else:
                    memo[word] = 1
            
            reverse = word[::-1]
            # 만약에 'xx'같이 반복된 문자열이면 따로 set에 저장 하고 나중에 따로 처리
            if len(set(word)) == 1:
                same.add(word)
            # 반대로 뒤집은 값이 memo 에 있으면 한 쌍으로 취급해서 answer에 값을 더해주고, value는 -1 하기,
            # valeu 가 0 이면 한쌍으로 취급받지 못함
            elif reverse in memo:
                if memo[reverse] != 0:
                    answer += 4
                    memo[reverse] -=1
                    memo[word] -=1
                elif memo[reverse] == 0:
                    continue

        # 'xx'가 2개 이상인 경우 짝수개만큼 더하고
        #  혹시 홀수개가 있따면 따로 하나를 더함
        #  홀수개는 하나밖에 넣을 수 없기 때문
        odd = 0
        for word in same:
            num = memo[word]
            if num%2 == 0:
                answer += num*2
            else:
                answer += (num-1)*2
                odd = 2

        return answer+odd
    
solution = Solution()
print(solution.longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        double = 0
        ans = 0
        for word, count in counter.items():
            if word[0] == word[1]:
                if count % 2:
                    ans += 2 * (count - 1)
                    double = 2
                else:
                    ans += 2 * count
            elif word[0] < word[1]:
                ans += 4 * min(count, counter[word[::-1]])
        return ans + double