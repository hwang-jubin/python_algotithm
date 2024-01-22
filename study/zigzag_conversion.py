# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for _ in range(numRows)]
        r = 0
        index = 0

        # numRow가 0 일 때 무한루프에 빠짐 방지
        if numRows == 1:
            return s
        
        while(index < len(s)):
            # 수직하강
            while r < numRows-1 and index < len(s) :
                arr[r].append(s[index])
                index+=1
                r+=1
            # 대각선
            while r > 0 and index < len(s):
                arr[r].append(s[index])
                index+=1
                r-=1

        answer = ""

        for i in arr:
            for j in i:
                answer+=j
        return answer
    
solution = Solution()
solution.convert(s = "A", numRows = 1)