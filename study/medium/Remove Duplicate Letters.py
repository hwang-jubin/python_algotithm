# https://leetcode.com/problems/remove-duplicate-letters/?envType=daily-question&envId=2024-01-20

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Step 1: 각 문자의 출현 횟수를 세기
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Step 2: 스택을 사용하여 중복 문자 제거
        stack = []
        seen = set()  # 이미 스택에 있는 문자 집합
        for char in s:
            count[char] -= 1  # 문자 출현 횟수 감소
            if char in seen:
                continue
            # 스택이 비어있지 않고, 스택의 맨 위 문자가 현재 문자보다 사전적으로 크며, 이후에 해당 문자가 또 나오면 스택에서 제거
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        # Step 3: 최종 결과 반환
        return ''.join(stack)

solution = Solution()
print(solution.removeDuplicateLetters(s="bcabc"))  # 출력: 'abc'
