# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# time limit 
from collections import deque

def solution(n, left, right):
    matrix = [[0]*n for _ in range(n)]
    memo = [[False]*n for _ in range(n)]

    # 오른쪽, 대각선, 아래
    dir = [(0,1), (1,1), (1,0)]
    q = deque()
    q.append((0,0))
    a = 1
    # matrix[0][0] = 1
    while q and a < n:
        s = len(q)
        temp = []
        for i in range(s):
            r,c = q.popleft()
            temp.append((r,c))
            
            for row,col in dir:
                dr = r+row
                dc = c+col
                if n>dr>=0 and n>dc>=0:
                    if memo[dr][dc] == False:
                        q.append((dr,dc))
                        memo[dr][dc] = True
        
        for (pr,pc) in temp:
            matrix[pr][pc] = a
        
        a = a+1

    number = 0

    answer = []
    for i in range(n):
        for j in range(n):
            if left<=number<=right:
                answer.append(matrix[i][j])
            elif number>right:
                break
            number+=1
        if number >right:
            break

    return answer



print(solution(n=4, left = 7, right = 14))


# 행과 열중에 큰 값+1이 채워지는 값
def solution(n, left, right):
    result = []
    for num in range(left, right + 1):
        row = num // n  # 현재 숫자가 몇 번째 행에 속하는지 계산
        col = num % n  # 현재 숫자가 몇 번째 열에 속하는지 계산
        value = max(row, col) + 1  # 행과 열 중 큰 값에 1을 더한 것이 해당 좌표의 값
        result.append(value)
    return result

# 예시 테스트
print(solution(n=4, left=7, right=14))  # [4, 3, 3, 3, 4, 4, 4, 4]
