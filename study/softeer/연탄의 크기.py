import sys

n = map(int ,sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
max_num=max(arr)
max_y = 0
for i in range(2,max_num+1):
    num = 0
    for a in arr:
        if a%i == 0 :
            num+=1
    max_y = max(max_y,num)

print(max_y)
