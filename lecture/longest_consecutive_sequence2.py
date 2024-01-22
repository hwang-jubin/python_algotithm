# list 오름차순
class Solution:
    def sequence(self, nums):
        answer = 0
        nums.sort()
        cnt = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                cnt += 1 
            else:
                answer = max(answer, cnt)
                cnt = 1

        return answer


solution_instance= Solution()
print(solution_instance.sequence(nums=[1,3,4,5,6,9,11]))