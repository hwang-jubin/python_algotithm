from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        shorted_len = -1
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False]*col_len for _ in range(row_len)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # 출발점과 도착점이 1이면 경로가 없어서 -1 반환
        if grid[0][0] == 1 or grid[row_len-1][col_len-1]==1:
            return shorted_len

        q = deque()
        q.append((0,0,1))

        # 범위를 벗어났는지 체크
        def check(next_r, next_l):
            return 0<=next_r<row_len and 0<= next_l <col_len

        while q:
            r, l, length = q.popleft()
            # 마지막 경로까지 갔으면 가장 단거리라서 루프 빠져나감
            if r == row_len-1 and l == col_len-1:
                shorted_len = length
                break
            # 좌우위아래대각선까지 모두 검사
            for dr, dl in directions:
                next_r = r+dr
                next_c = l+dl

                if check(next_r, next_c):
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        q.append((next_r,next_c,length+1))
                        visited[next_r][next_c] = True
        
        return shorted_len
    

solution = Solution()
print(solution.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))