# https://leetcode.com/problems/partition-list/

from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x: int):
        head_up = ListNode(0)
        head_down = ListNode(0)
        up = head_up
        down = head_down

        current = head
        while current:
            if current.val < x:
                down.next = current
                down = current
            elif current.val >=x:
                up.next = current
                up = current
            current = current.next
        
        # 마지막을 None으로 끊어줘야지 순환되지 않음
        up.next = None
        # 작은 node의 마지막과 큰 노드의 맨 앞(head)의 그 다음을 연결 하기
        down.next = head_up.next
        # head는 dommy node라서 그 다음 node을 반환
        return head_down.next

            
solution = Solution()
solution

