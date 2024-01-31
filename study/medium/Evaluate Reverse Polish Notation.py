# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens) -> int:
        answer = 0
        stk = []
        for index,value in enumerate(tokens):
            if value == "/":
                r = stk.pop()
                l = stk.pop()
                a = int(l / r)
                stk.append(a)
            elif value == "+":
                r = stk.pop()
                l = stk.pop()
                stk.append(l+r)
            elif value == "-":
                r = stk.pop()
                l = stk.pop()
                stk.append(l-r)
            elif value =="*":
                r = stk.pop()
                l = stk.pop()
                stk.append(l*r)
            else:
                stk.append(int(value))
        answer = stk[0]

        return answer
solution = Solution()
print(solution.evalRPN(tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))



        