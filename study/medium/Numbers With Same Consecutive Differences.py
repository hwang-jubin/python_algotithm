# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        answer = []
        def bt(num, s):

            if len(s) == n:
                answer.append(int(s))
                return
                        
            if num + k < 10:
                bt(num+k, s+str(num+k))
            if num - k >= 0 and k != 0:
                bt(num-k, s+str(num-k))

        for i in range(1,10):
                s=str(i)
                bt(i,s)

        return answer

solution = Solution()
print(solution.numsSameConsecDiff(n = 3, k = 0))