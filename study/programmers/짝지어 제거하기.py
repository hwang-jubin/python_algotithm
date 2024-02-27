def solution(s):
    stk = []
    
    for c in s:
        if len(stk) == 0:
            stk.append(c)
        else:
            if stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)

    if stk:
        return 0
    else:
        return 1
            
print(solution("aacdcd"))