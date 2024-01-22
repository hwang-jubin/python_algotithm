# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1:"I" ,5:"V", 10:"X", 50:"L", 100:"C", 500:"D" ,1000:"M"}
        str_memo = ""

        # 자리수 구하기
        num_copy = num
        power = 0
        while num_copy > 10:
            num_copy //= 10
            power += 1

        # 170
        while power >= 0 :
            num_at= (num//(10**power))*(10**power)
            num=num%(10**power)

            if num_at in roman:
                str_memo+=roman[num_at]
                power-=1
            elif num_at ==0:
                power-=1  
            else:    
                max_num = min((i for i in roman if i > num_at), default=None)
                if max_num is not None:
                    minus = max_num - num_at
                    if minus in roman:
                        str_memo+= roman[minus]
                        str_memo+= roman[max_num]
                    else:
                        while num_at !=0:
                            min_num = max((i for i in roman if i <= num_at))
                            num_at = num_at - min_num 
                            str_memo+=roman[min_num]
                elif max_num == None:
                    while num_at !=0:
                        str_memo+=roman[1000]
                        num_at -= 1000
                power-=1
        return str_memo
    
solution = Solution()
solution.intToRoman(num =2000)