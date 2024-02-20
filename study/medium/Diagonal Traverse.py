# https://leetcode.com/problems/diagonal-traverse/description/

class Solution:
    def findDiagonalOrder(self, mat):
        len_r = len(mat)
        len_c = len(mat[0])

        answer = []
        def recur(r,c,bool):
            nonlocal len_r
            nonlocal len_c
            
            if r==len_r or c==len_c:
                return 

            while r>=0 and r<len_r and c>=0 and c<len_c:
                answer.append(mat[r][c])
                if bool:
                    r = r-1
                    c = c+1
                else:
                    r = r+1
                    c = c-1

            if r < 0 and c < len_c:
                r = r+1
                bool = False
            elif c == len_c:
                r = r+2
                c = c-1
                bool = False
            elif c < 0 and r < len_r:
                c = c+1
                bool = True
            elif r == len_r: 
                r = r-1
                c = c+2
                bool = True

            recur(r,c,bool)

                
        bool = True
        recur(0,0,bool)
        return answer

solution = Solution()
print(solution.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))