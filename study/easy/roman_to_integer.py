# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {"I":1 ,"V":5, "X":10, "L":50, "C":100, "D":500 ,"M":1000}
        answer = 0 
        ren = 0

        for i in range(len(s)-1 , -1, -1):
            num = roman[str[i]]
            if num <ren :
                answer -= num 
            else:
                answer += num
            
            ren = roman[str[i]]
        
        return answer