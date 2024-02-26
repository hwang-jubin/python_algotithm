# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    memo = {}  # 메모이제이션을 위한 딕셔너리

    def dfs(index, total):
        # 기저 사례: 모든 숫자를 다 사용한 경우
        if index == len(numbers):
            # 타겟 숫자에 도달했으면 1을 반환하고, 아니면 0을 반환
            return 1 if total == target else 0

        # 이미 계산한 적이 있는 경우, 메모이제이션된 값을 반환
        if (index, total) in memo:
            return memo[(index, total)]

        # 현재 숫자를 더하거나 빼는 두 가지 경우를 탐색
        add = dfs(index + 1, total + numbers[index])
        subtract = dfs(index + 1, total - numbers[index])

        # 현재 상태에 대한 결과를 메모이제이션
        memo[(index, total)] = add + subtract

        return memo[(index, total)]

    # 인덱스 0부터 시작하여 재귀 함수 호출
    return dfs(0, 0)

# 테스트
print(solution([1, 1, 1, 1, 1], 3))  # 출력: 5
