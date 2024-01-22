# bottom-up , bp

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1]*n for _ in range(m)]

        memo[0][0] = 1

        for r in range(0,m):
            for c in range(0,n):
                if r == 0 and c == 0:
                    continue
                path = 0
                if r-1>=0:
                    path+= memo[r-1][c]
                if c-1>=0:
                    path+= memo[r][c-1]
                memo[r][c] = path

        return memo[m-1][n-1]
    
# out of bound 인지 검사하지 않는 방법
# Bottom-up:
class Solution:
    def uniquePaths(self, m, n):
        memo = [[-1] * n for _ in range(m)]
        for r in range(m):
            memo[r][0] = 1
        for c in range(n):
            memo[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                memo[r][c] = memo[r - 1][c] + memo[r][c - 1]

        return memo[m - 1][n - 1]