# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1]*len(numbers)

    stk = []

    for index in range(len(numbers)):
        if stk:
            number, i = stk[-1]
            if number < numbers[index]:
                while number < numbers[index]:
                    answer[i] = numbers[index]
                    stk.pop()
                    if stk:
                        number,i = stk[-1]
                    else:
                        break

        stk.append((numbers[index],index))

    return answer

print(solution([2, 3, 3, 5]))