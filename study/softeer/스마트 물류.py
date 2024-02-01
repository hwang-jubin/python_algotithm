import sys

n,k = map(int, sys.stdin.readline().split())

s = sys.stdin.readline().strip()

q = set()

answer = 0

for index,value in enumerate(s):
    if value == 'H':
        q.add(index)
        

for index,value in enumerate(s):
    if value == 'P':
        flag = True
        for i in range(k,0,-1):
            if index - i in q:
                q.remove(index-i)
                answer+=1
                flag = False
                break
        if flag:
            for i in range(1,k+1):
                if index +i in q:
                    q.remove(index+i)
                    answer+=1    
                    break
    

print(answer)



