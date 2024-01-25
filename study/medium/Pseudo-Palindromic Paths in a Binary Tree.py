# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/submissions/1155624539/?envType=daily-question&envId=2024-01-24


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root) -> int:
        memo = {}
        answer = 0
        def bt(root, memo):
            nonlocal answer
    
            if root == None:
                return
            
            # 전위순회
            if root.val not in memo:
                memo[root.val] = 1
            else:
                memo[root.val] +=1

            # 말단 노드
            if root.left == None and root.right == None:
                # 회문검사
                # 홀수가 0,1 개 -> 회문, 2개 이상이면 회문 아님
                odd = 0
                for num in memo:
                    if memo[num]%2 !=0:
                        odd+=1
                    if odd > 1 :
                        break
                                        
                if odd < 2:
                    answer+=1
            else:
                if root.left != None:
                    bt(root.left, memo)
                if root.right != None:
                    bt(root.right, memo)

            memo[root.val] -= 1

        bt(root, memo)

        return answer
    

# 테스트 케이스 생성
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)

solution = Solution()
solution.pseudoPalindromicPaths(root)