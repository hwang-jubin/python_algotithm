#graph bps 구현
#root부터 가장 가까운 node들 부터 순회
#graph 는 dictionay 로 저장
from Collections import deque
#  start node 는 dictionary의 key
class Solution:
    def bps(self, graph, start_node):
        visited = [start_node]
        if graph is None:
            return visited
        q = deque()
        q.append(start_node)

        while q:
            node = q.popleft()
            for v in graph[node]:
                if v not in visited:
                    visited.append(v)
                    q.append(v)
        return visited
