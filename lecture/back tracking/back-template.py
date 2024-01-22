def dt(nums):
    answer = []
    def backtracking(start, cur):
            if len(cur) == k:
                answer.append(cur[:])
                return
            #  배열에 값을 담았다가 완성이 되면 answer에 저장을 하고, 그 다음 조합을 위해서 pop 한 후 다음 조합 시행
            #  3개라고 했을 때, 처음에는 0부터 넣고 , 
            for i in range(start, len(nums)):    
                cur.append(nums[i])
                backtracking(i+1, cur)
                cur.pop()

    # 0부터 nums 의 크기만큼 전부 다 부분집합 만들기
    for k in range(len(nums)+1):
        # 임시 배열 전달
        backtracking(start=0, cur = [])

    return answer

print(dt(nums = [1,2,3,4]))