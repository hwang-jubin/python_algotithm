class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        memo = {}
        for i in arr:
            if i in memo:
                memo[i]+=1
            else:
                memo[i]=1

        a = set()
        for i in memo.values():
            if i in a:
                return False
            else:
                a.add(i)
        return True

solution = Solution()
solution.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])