# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        key = ListNode()
        current = head
        while current:
            prev = key
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            next_list = current.next
            current.next = prev.next
            prev.next = current
            current = next_list
        return key.next
