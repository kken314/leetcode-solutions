# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid point
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # disconnect
        second = slow.next
        slow.next = None
        # reverse second half
        prev = None
        while second:
            front = second.next
            second.next = prev
            prev = second
            second = front
        # merge
        first = head
        second = prev
        while second:
            front1 = first.next
            first.next = second

            front2 = second.next
            second.next = front1

            first = front1
            second = front2
            
            