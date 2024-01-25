# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return None

        q = deque()
        q.append(root)
        
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i < length - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


        return root