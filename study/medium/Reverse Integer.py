class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        minus = '-'
        if 48<=ord(string[0])<=57:
            string = string[::-1]
            answer = int(string)
        else:
            string = string[1::]
            string = string[::-1]
            answer = -1*int(string)

            return answer
        

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10

        reversed_num *= sign

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num



solution = Solution()
solution.reverse(x=-123)