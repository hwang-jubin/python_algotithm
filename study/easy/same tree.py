# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        answer = True

        def dfs(node1, node2):
            nonlocal answer

            if not node1 and not node2:
                return

            if (not node1 or not node2) or (node1.val != node2.val):
                answer = False
                return

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

        dfs(p, q)
        return answer


root=TreeNode(1)
node4=TreeNode(2)
node5=TreeNode(3)
root.left = node4
root.right = node5

root2=TreeNode(1)
node3=TreeNode(2)
node4=TreeNode(3)
root2.left = node3
root2.right = node4

solution = Solution()
solution.isSameTree(root, root2)