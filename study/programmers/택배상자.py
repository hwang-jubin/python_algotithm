# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    origin = 1
    temp =[]
    index = 0

    while origin!= len(order)+1:
        temp.append(origin)
        while temp[-1] == order[index]:
            index+=1
            temp.pop()
            if len(temp) == 0:
                break
        origin+=1


    return index

print(solution([5, 4, 3, 2, 1]))