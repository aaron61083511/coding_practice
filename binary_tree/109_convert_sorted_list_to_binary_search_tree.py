# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        pointer = head
        count = 0
        while pointer:
            count += 1
            pointer = pointer.next

        def helper(l, r):
            nonlocal head
            if l > r:
                return None
            mid = (l + r) // 2
            left = helper(l, mid-1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = helper(mid+1, r)
            return node

        return helper(0, count-1)