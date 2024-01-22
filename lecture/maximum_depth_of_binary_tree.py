
#BFS(너비우선 탐색)

class Solution:
    def traversal(self, root):
        depth = 0
        if root is None:
            return depth
        
        q = deque()
        q.append((root, 1))
        
        while q :
            cur_node , node_depth = q.popleft()
            depth = node_depth
            if cur_node.left:
                q.append((cur_node.left , node_depth+1))
            if cur_node.right:
                q.append((cur_node.right , node_depth+1))
            
        return depth


class Tree_node:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v


root = Tree_node(v = 3)
root.left = Tree_node(v=9)
root.right = Tree_node(v=20)
solution = Solution()
solution.traversal(root)

# postorder(후위순회) 재귀

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        left_max= self.maxDepth(root.left)
        right_max= self.maxDepth(root.right)
        max_depth = max(left_max,right_max)+1
        return max_depth