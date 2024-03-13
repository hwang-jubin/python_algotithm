def solution(want, number, discount):
    answer = 0

    def check(date):
        memo = {}
        for i in range(date, date + 10):
            if discount[i] in memo:
                memo[discount[i]] += 1
            else:
                memo[discount[i]] = 1

        for i in range(len(want)):
            if want[i] not in memo or memo[want[i]] < number[i]:
                return False
        return True

    for i in range(len(discount) - 9):
        if check(i):
            answer += 1

    return answer

