import math

class Solution:
    def constructRectangle(self, area: int):
        for i in range(int(math.sqrt(area)),0,-1):
            if area % i == 0 :
                return [area//i , i]

solution = Solution()
print(solution.constructRectangle(area=37))