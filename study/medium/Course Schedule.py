# https://leetcode.com/problems/course-schedule/
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # node를 선행해야 하는 node 목록
        # 예시) 0 과목을 듣기 위해서 선행해야 하는 과목들을 index = 0에 [1] 
        memo = [[] for _ in range(numCourses)]
        # index를 선행으로 하는 과목들의 개수 
        memo_num = [0]*numCourses

        for pre in prerequisites:
            memo_num[pre[0]] +=1
            memo[pre[1]].append(pre[0])

        q = deque()
        for i in range(numCourses):
            if memo_num[i] == 0:
                q.append(i)
        
        visited = 0
        while q:
            node = q.popleft()
            visited+=1
            for i in memo[node]:
                memo_num[i]-=1
                if memo_num[i]==0:
                    q.append(i)
        return numCourses == visited

solution = Solution()
solution.canFinish(numCourses = 4, prerequisites = [[0,1],[1,0],[2,3]])