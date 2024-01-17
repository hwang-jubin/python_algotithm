# hashSet
# dictionary 로도 구현 가능
class Solution:
    def sequence(self, nums):
        answer = 0
        hash = set(nums)
        for i in nums:
            if i-1 not in hash:
                cnt = 1
                target = i+1
                while target in hash:
                    cnt+=1
                    target+=1
                answer = max(answer, cnt)

        return answer


solution_instance= Solution()
print(solution_instance.sequence(nums=[1,2,3,4,6,7,8,9,10]))