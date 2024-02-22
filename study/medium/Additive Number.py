# https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(index, num1 , num2):

            sum = num1, num2
            sum_str = str(sum)
            next_len = len(sum_str)
            # 다음 숫자의 index가 num 의 길이보다 크면 유효하지 않고
            # 또는 더한 숫자가 같지 않으면 유효하지 않음
            if index+next_len > len(num) or num[index:index + next_len] != sum_str:
                return False
        
            return dfs(index+next_len, num2, sum)

        # 첫번째, 두번째 숫자에 대한 로직
        for i in range(1,len(num)):
            for j in range(i+1, len(num)):   
                num1 = num[:i]
                num2 = num[i:j]
                # 길이가 2 이상인데 첫번째 숫자가 0이면 유효하지 않은 숫자
                # 길이가 1일 때 첫번째 숫자가 0이면 그냥 0
                if (len(num1)>1 and num1.startswith("0")) or (len(num2)>1 and num2.startswith("0")):
                    continue
                # 다음은 dfs
                if dfs(j, int(num1), int(num2)) :
                    return True
                
        return False
    

solution = Solution()
solution.isAdditiveNumber(num="1257")