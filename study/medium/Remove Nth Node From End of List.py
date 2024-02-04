# 정의된 ListNode 클래스
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 클래스 정의
class Solution:
    def removeNthFromEnd(self, head, n: int):
        # 더미 노드 생성 및 연결 리스트 연결
        dummy = ListNode(0)
        dummy.next = head
        # 두 개의 포인터 초기화
        slow = dummy
        fast = dummy

        # fast 포인터를 n + 1번 앞으로 이동
        for _ in range(n + 1):
            fast = fast.next

        # slow와 fast 포인터를 함께 이동하여 fast가 끝에 도달할 때까지 진행
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # 뒤에서 n번째 노드를 삭제
        slow.next = slow.next.next

        # 업데이트된 헤드 반환
        return dummy.next

# 예시로 사용할 연결 리스트 생성
head = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(3)
head4 = ListNode(4)
head5 = ListNode(5)

head.next = head2
head2.next = head3
head3.next = head4
head4.next = head5

# Solution 객체 생성 및 removeNthFromEnd 메서드 호출
solution = Solution()
new_head = solution.removeNthFromEnd(head, 2)

# 결과 확인
while new_head is not None:
    print(new_head.val, end=" ")
    new_head = new_head.next
