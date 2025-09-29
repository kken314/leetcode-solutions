# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_A = set()
        curr_A, curr_B = headA, headB
        
        while curr_A:
            visited_A.add(curr_A)
            curr_A = curr_A.next

        while curr_B:
            if curr_B in visited_A:
                return curr_B
            curr_B = curr_B.next        
        return None
