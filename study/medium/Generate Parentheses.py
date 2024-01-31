# https://leetcode.com/problems/generate-parentheses/description/
# 1. ( 다음에는 )가 나온다는 컨셉
# 2. (가 n개까지 나오지 않는 이상 )가 올 수 있음 -> right > left 가 될 수 없음
# 3. right > left 일 때까지만 )를 추가하고 다시 left 가 n 개가 될때까지 ( 를 추가 할 수 있음


class Solution:
    def generateParenthesis(self, n: int):
        answer = []
        def bt(left, right , s):

            if len(s) == n*2:
                answer.append(s)
                return
            
            if left < n:
                bt(left+1, right, s+'(')
            
            if right < left:
                bt(left, right+1, s+')')


        s = ""
        bt(0,0,s)