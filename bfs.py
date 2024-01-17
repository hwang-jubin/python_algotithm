from collections import deque
class solution:
    def bfs(self, root):
        visit = []
        if root is None :
            return visit
        que = deque()
        que.append(root)
        while que:
            cur_node = que.popleft()
            visit.append(cur_node.value)

            if cur_node.left:
                que.append(cur_node.left)
            elif cur_node.right:
                que.append(cur_node.right)
            
        return visit



