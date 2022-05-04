# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        current, prev = head, None

        while left > 1:
            prev = current
            current = current.next
            left -= 1
            right -= 1

        tail, con = current, prev

        while right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            right -= 1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = current

        return head

