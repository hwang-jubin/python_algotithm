from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        # 그래프와 진입 차수 초기화
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        # 진입 차수가 0인 노드를 큐에 추가
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # 위상 정렬 수행
        order = []  # 과목을 방문하는 순서를 저장할 리스트
        while queue:
            node = queue.popleft()
            order.append(node)  # 과목을 방문하는 순서를 기록
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 모든 노드를 방문했으면 순서 리스트 반환, 그렇지 않으면 빈 리스트 반환
        return order if len(order) == numCourses else []


solution = Solution()
solution.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
