# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True

        q = deque()
        q.append(root)

        while q:
            level_values = []

            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level_values.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level_values.append(None)

            # 대칭 여부 확인
            length = len(level_values)
            for i in range(length // 2):
                if level_values[i] != level_values[length - 1 - i]:
                    return False

        return True
    
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node5
node2.left = node6
node2.right = node4
    


# root = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(3)

# root.left = node1
# root.right = node2
# node1.right = node3
# node2.right = node4

solution = Solution()
print(solution.isSymmetric(root))