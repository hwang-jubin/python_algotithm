class Solution:
    def isValid(self, s):
        stk = []
        for i in s:
            if i == '{':
                stk.append('}')
            elif i == '[':
                stk.append(']')
            elif i == '(':
                stk.append(')')
            elif stk and stk[-1]==i:
                stk.pop()
            else:
                return False
        

        return not stk

solution_instance = Solution()
result = solution_instance.isValid("{{[()]}}")