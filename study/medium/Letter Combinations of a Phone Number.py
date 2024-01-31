# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str):
        
        memo = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

        arr = []

        for char in digits:
            a=memo[int(char)]
            arr.append(a)

        answer = []
        leng = len(arr)
        if leng == 0:
            return answer



        # arr에 memo의 index에 해당하는 list를 저장해놓고 arr를 다 돌때 까지 backtracking
        # index를 넘겨줘서 다음 index에서 모든 경우의 수가 다 돌 수 있도록 했음 
        def dfs(index,s):
            nonlocal leng
            if index >= leng:
                answer.append(s)
                return
            array_a = arr[index]
            for char in array_a:
                dfs(index+1, s+char)

        index = 0
        s = ""
        dfs(index,s)

        return answer

solution = Solution()
print(solution.letterCombinations(digits = "23"))