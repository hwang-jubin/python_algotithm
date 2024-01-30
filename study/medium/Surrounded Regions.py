# https://leetcode.com/problems/surrounded-regions/

# 0인데 x에 둘러싸이지 않는 경우는 가장자리에 있는 O의 그룹
# 가장자리에 있는 O그룹을 다 탐색하고 T라고 표시
# 안쪽에 있는 O들은 둘러싸인거라고 간주하고 X로 변환
# T들은 O으로 바꿔주기

class Solution:
    def solve(self, board) -> None:
        row_len = len(board)
        col_len = len(board[0])
        def dfs(r,c):
            
            if r<0 or r==row_len or c<0 or c==col_len or board[r][c] != "O":
                return 

            board[r][c] = "T"

            dir = [(-1,0),(0,1),(1,0),(0,-1)]
            for a,b in dir:
                dfs(a+r,b+c)
            
        # 가장자리에 있는데 0 인경우 주변 0 들을 T로 만들어 줘야 함
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] =="O" and ( i in [0,row_len-1] or j in [0, col_len-1]):
                    dfs(i,j)

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] =="O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"

solution = Solution()
solution.solve(board = [["O","O","O"],["O","O","O"],["O","O","O"]])



class Solution:

    def solve(self, board: List[List[str]]) -> None:
        n_rows, n_cols = len(board), len(board[0])

        # all "O"s in the border are unsurrounded, we find these, then traverse adjacent "O"s
        def dfs(r, c):
            if r < 0 or r == n_rows or c < 0 or c == n_cols or board[r][c] != "O":
                return
          
            board[r][c] = "T" # these are unsurrounded
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "O" and (r in [0, n_rows - 1] or c in [0, n_cols - 1]):
                    dfs(r, c)

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "O": # surrounded, since can't reach border
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
