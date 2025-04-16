# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        head = ListNode()
        curr = head
        while node1 and node2:
            if node1.val <= node2.val:
                curr.next = node1
                node1 = node1.next
            elif node1.val > node2.val:
                curr.next = node2
                node2 = node2.next
            curr = curr.next
        
        if node1:
            curr.next = node1
        else:
            curr.next = node2

        return head.next
