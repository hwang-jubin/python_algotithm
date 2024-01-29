
class Solution:
    def countBits(self, n: int):
        arr = []
        for i in range(n+1):
            num = 1
            if i <= 1:
                arr.append(i)
                continue
            quo = i
            rem = 0 
            while quo > 1:
                quo = i//2
                rem = i%2
                if rem == 1:
                    num+=1
                i = quo
            arr.append(num)
        return arr 

solution = Solution()
solution.countBits(n=2)


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            b = bin(i)[2:]
            result.append(b.count('1'))
        return result