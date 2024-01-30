# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs로 같은 level에 있는 node들을 append 한 후
# 같은 level의 q에 있는 node를 제거 할 때 마지막 pop 되는 node 가 오른쪽에서 볼 때 첫번째로 보이는 node

class Solution:
    def rightSideView(self, root):
        q = deque()
        if root ==None:
            return q
        q.append(root)
        answer = []
        while q:
            size = len(q)

            for i in size:
                node = q.popleft()
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if i == size-1:
                    answer.append(node.val)
        return answer









    
        