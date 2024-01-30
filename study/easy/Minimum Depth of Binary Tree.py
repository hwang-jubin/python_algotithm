# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root) -> int:
        
        q = deque()
        q.append(root)
        dep= 1
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()

                if node.left is None and node.right is None:
                    return dep

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            dep+=1
            
        return dep



root = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

root.left = node9
root.right = node20
node20.left = node15
node20.right = node7


solution = Solution()
solution.minDepth(root)

