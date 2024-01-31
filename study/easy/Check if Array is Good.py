# https://leetcode.com/problems/check-if-array-is-good/

class Solution:

    def isGood(self, nums) -> bool:
        length = 0
        # 가장 큰 수만큼 배열 만들기
        for i in nums:
            length =max(length, i)
        arr = [0]*length
        # 각 숫자당 몇개씩 나왔는지 저장
        for i in nums:
            arr[i-1]+=1

        # 각 숫자당 하나씩 나와야 하고 가장 큰 수는 2번 나와야 함
        # 각 숫자당 하나도 안나오거나 하나 이상 나오면 False
        for index, value in enumerate(arr):
            if (index+1)!=length and value !=1:
                return False
            elif (index+1) == length and value !=2:
                return False 
        return True
    

solution = Solution()
solution.isGood(nums = [2, 1, 3])