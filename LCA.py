class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode" ) -> "TreeNode":
        if root == None:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if root.val == p.val or root.val == q.val:
            return root
        elif left and right:
            return root
        else:
            return left or right
        
# 배열 이진트리 만들기
# class TreeNode:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def array_to_tree(nums, index=0):
#     if index < len(nums):
#         if nums[index] is None:
#             return None
#         root = TreeNode(nums[index])
#         root.left = array_to_tree(nums, 2 * index + 1)
#         root.right = array_to_tree(nums, 2 * index + 2)
#         return root
#     return None

# # 주어진 배열
# array_representation = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

# # 배열을 이진 트리로 변환
# root_node = array_to_tree(array_representation)

# # 예시: 변환된 트리의 루트 노드 값 출력
# print(root_node.val)  # 3
