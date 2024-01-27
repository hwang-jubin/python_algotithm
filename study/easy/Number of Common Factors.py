import math

class Solution:


    def commonFactors(self, a: int, b: int) -> int:
        answer = 0
        max_n = max(a, b)
        min_n = min(a, b)

        if max_n % min_n != 0:
            a = min_n
            b = max_n % min_n
        
            while True:
                if a % b != 0:
                    ren = a
                    a = b
                    b = ren % b
                else:
                    break
        else:
            b = min_n
        if b == 1:
            return 1
        else:
            for i in range(1, b+1):
                if b%i == 0:
                    answer+=1
        return answer
solution = Solution()
print(solution.commonFactors(a= 32, b = 408))



class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        answer = 0

        # 두 수를 큰 수와 작은 수로 정렬
        if a < b:
            a, b = b, a

        # 최대공약수 계산
        while b != 0:
            a, b = b, a % b

        # 최대공약수로 나누어 떨어지는 수의 개수 찾기
        for i in range(1, a + 1):
            if a % i == 0:
                answer += 1

        return answer
