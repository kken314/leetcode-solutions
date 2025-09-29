# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # Find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_node = slow #mid node means the first element of the secound half 
        # if fast is None length of the list is even number
        if fast != None:
            slow = slow.next  
        # Reverse the secound half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        curr2 = prev

        curr1 = head
        while curr1 != mid_node:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return True
                