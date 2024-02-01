# https://softeer.ai/app/assessment/index.html?xid=81509&xsrfToken=cozi5gi7bRM4FLCHZayZJglX5kalG5If&testType=practice

import sys
import math
f = []
for i in range(3):
    line = sys.stdin.readline().strip()
    arrays = [int(i) for i in line.split()]
    f.append(arrays)


r_len = 3
c_len = 3
min_h = math.inf
for c in range(3):
    for i in range(1,4):
        sum=abs(i - f[c][0]) +abs(i - f[c][1])+abs(i-f[c][2])
        min_h = min(min_h, sum)
        sum=abs(i - f[0][c]) +abs(i - f[1][c])+abs(i-f[2][c])
        min_h = min(min_h, sum)

print(min_h)
    


