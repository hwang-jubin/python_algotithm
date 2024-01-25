# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1156178136/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        def linked(list1, list2 , node):

            if list1 == None and list2 == None:
                return None

            if list1 is None:
                s_node = ListNode(list2.val)
                node.next = list2
                linked(list1, list2.next, s_node)
                return
            elif list2 is None:
                f_node = ListNode(list1.val)
                node.next = list1
                linked(list1.next, list2 , f_node)
                return

            f = list1.val
            s = list2.val

            if f == s:
                f_node = ListNode(f)
                s_node = ListNode(s)
                node.next = f_node
                f_node.next = s_node

                linked(list1.next, list2.next , s_node)
            elif f < s:
                f_node = ListNode(f)
                node.next = f_node
            
                linked(list1.next, list2 , f_node)
            elif f > s :
                s_node = ListNode(s)
                node.next = s_node

                linked(list1, list2.next, s_node)

        node = ListNode()
        linked(list1, list2, node)
        return node
    


    
list1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
list1.next = node2
node2.next = node3

list2 = ListNode(1)
node4 = ListNode(3)
node5 = ListNode(4)
list2.next = node4
node4.next = node5


solution = Solution()
solution.mergeTwoLists(list1, list2)

