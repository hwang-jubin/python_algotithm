# 가장 깊은 node 부터 순회
# 전위탐색

class Solution:
    def dfs(self, graph, visited, node):
        visited.append(node)
        for v in graph(node):
            if v not in visited:
                self.dfs(graph, visited, v)
        return visited