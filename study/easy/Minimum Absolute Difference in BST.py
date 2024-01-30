# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root) -> int:
        min_num = math.inf
        # 중위순회
        def dfs(root, result):
            nonlocal min_num
            if root == None:
                return
            
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
            

        values = []
        dfs(root, values)

        for i in range(1,len(values)):
            min_num = min(min_num, values[i]-values[i-1])
        
        return min_num