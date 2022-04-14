# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        first_half_end = self.get_first_half(head)
        second_half_start = self.reverse(first_half_end.next)
        
        first_pos = head
        second_pos = second_half_start
        while second_pos is not None:
            if first_pos.val != second_pos.val:
                return False
            first_pos = first_pos.next
            second_pos = second_pos.next
        first_half_end.next = self.reverse(second_half_start)
        return True
    
    def get_first_half(self, head):
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
