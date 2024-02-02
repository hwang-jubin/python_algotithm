class Solution:
    def simplifyPath(self, path: str) -> str:

        stk = path.split('/')
        answer = []
        for s in stk:
            if s == '.' or s == '':
                continue
            elif s == '..':
                if answer:
                    answer.pop()
            else:
                answer.append(s)
            
        answer='/'+'/'.join(answer)
        return answer
solution = Solution()
solution.simplifyPath(path = "/hello/../abc/")