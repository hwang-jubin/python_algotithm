# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    memo = [[0]*len(land[0]) for _ in range(len(land))]

    for i in range(len(land[0])):
        memo[0][i] = land[0][i]

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            max_sum = 0
            for k in range(len(land[0])):
                if j!=k:
                    max_sum = max(max_sum, land[i][j]+memo[i-1][k])
            memo[i][j] = max_sum

    answer=max(memo[-1])
    return answer


# | 1 | 2 | 3 | 5 |

# | 5 | 6 | 7 | 8 |

# | 4 | 3 | 2 | 1 |

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))