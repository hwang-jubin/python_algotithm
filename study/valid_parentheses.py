# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        # stack 에 값이 있으면 pop 해서 비교
        # } ] ) 인데 stk 에 값이 없으면 False
        for i in s:
            if i == "{":
                stk.append("}")
            elif i == "(":
                stk.append(")")
            elif i == "[":
                stk.append("]")
            elif stk:
                a = stk.pop()
                if  a!= i :
                    return False
            else:
                return False
            
        return not stk