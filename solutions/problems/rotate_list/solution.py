# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        k = k % n
        if k == 0:
            return head
        curr = head
        for i in range(k):
            curr = curr.next
        prev = head
        while curr and curr.next:
            curr = curr.next
            prev = prev.next
        new_head = prev.next
        prev.next = None
        curr.next = head
        return new_head