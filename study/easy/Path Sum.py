# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        answer = False
        def dfs(root, sum):
            nonlocal answer
            if root is None:
                return 
            
            sum+=root.val
            dfs(root.left,sum)
            dfs(root.right,sum)
            
            if root.left == None and root.right == None:
                if answer :
                    return
                if sum == targetSum:
                    answer = True
                    return

        sum = 0
        dfs(root, sum)
        return answer
    
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
solution.hasPathSum(root, targetSum = 30)