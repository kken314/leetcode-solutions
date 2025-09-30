# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prev = dummy

        while curr and curr.next:
            front = curr.next
            prev.next = curr.next
            curr.next = curr.next.next
            front.next = curr
            
            prev = curr
            curr = curr.next
        return dummy.next