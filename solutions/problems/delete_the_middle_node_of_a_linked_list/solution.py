# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        del_index = count // 2
        curr = head
        prev = None
        for i in range(del_index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head
        
        
        