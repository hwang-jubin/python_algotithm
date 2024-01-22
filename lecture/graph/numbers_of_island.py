from collections import deque

#BFS
class Solution:
    def numIslands(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        
        visited = [[False]*col for _ in range(row)]
        answer = 0

        def bfs(r, c , grid):
            # 아래, 오른쪽, 위, 왼쪽
            dr = [1,0,-1,0]
            dc = [0,1,0,-1]
            

            q = deque()
            q.append((r, c))
            visited[i][j] = True
            while q:
                cur_r, cur_c = q.popleft()
                for num in range(4):
                    next_r = cur_r+dr[num]
                    next_c = cur_c+dc[num]

                    if next_r >= 0 and next_r < len(grid) and next_c>=0 and next_c < len(grid[0]):
                        if not visited[next_r][next_c] and grid[next_r][next_c] == '1':
                            visited[next_r][next_c] = True
                            q.append((next_r, next_c))


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and visited[i][j] is False:
                    bfs(i, j, grid)
                    answer+=1

        return answer


solution = Solution()
print(solution.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]))