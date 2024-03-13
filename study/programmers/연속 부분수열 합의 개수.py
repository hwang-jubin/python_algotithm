# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = set()

    def sum(count):
        length = len(elements)
        s = 0
        for i in range(count):
            s+=elements[i]
        
        answer.add(s)
        
        for i in range(1,length):
            s-=elements[i-1]
            index = (i+count-1)%length
            s+=elements[index]
            answer.add(s)

    for i in range(len(elements)):
        answer.add(elements[i])


    for i in range(2,len(elements)+1):
        sum(i)

    return len(answer)

print(solution([7,9,1,1,4]))
