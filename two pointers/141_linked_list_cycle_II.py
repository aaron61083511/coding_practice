# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        if head is None:
            return None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        inter = slow
        if fast == None or fast.next == None:
            return None

        p1 = head
        p2 = inter
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
