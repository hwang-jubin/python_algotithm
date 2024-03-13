
# 시간복잡도 높음 - O(n제곱)
def solution(phone_book):

    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            r = max(phone_book[i],phone_book[j])
            s = min(phone_book[i],phone_book[j])
            ls = len(s)
            r = r[0:len(s)]
            if r == s:
                return False
    return True

solution(["119", "97674223", "1195524421"])

def solution(phone_book):
    memo = set()
    for i in phone_book:
        memo.add(i)


    for number in phone_book:
        prefix = ""
        for n in number:
            prefix += n
            if prefix in memo and prefix != number:
                return False
            
    return True
