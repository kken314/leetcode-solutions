# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLinkLists(self, head1, head2):
        head = ListNode()
        curr = head
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head2:
            curr.next = head2
        else:
            curr.next = head1
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            MergeLists = []
            for i in range(0, len(lists) - 1, 2):
                MergeLists.append(self.mergeLinkLists(lists[i], lists[i+1]))
            if len(lists) % 2 == 1:
                MergeLists.append(lists[-1])
            lists = MergeLists
        return lists[0]       