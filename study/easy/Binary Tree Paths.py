# https://leetcode.com/problems/binary-tree-paths/
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []

        def bt(node, path):
            if node is None:
                return

            # 현재 노드의 값을 string 으로 바꾸어 경로에 추가
            path.append(str(node.val))

            # 리프 노드에 도달했을 때, 현재 경로를 정답에 추가
            if node.left is None and node.right is None:
                answer.append("->".join(path))

            # 왼쪽 자식 노드로 이동
            bt(node.left, path)
            # 오른쪽 자식 노드로 이동
            bt(node.right, path)

            # 현재 노드의 값을 경로에서 제거 (backtrack)
            path.pop()

        bt(root, [])

        return answer
