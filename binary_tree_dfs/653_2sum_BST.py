# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack, seen = [root], set()

        while stack:
            curr = stack.pop()
            # If we've seen k - curr.val,
            # we have k - curr.val + curr.val = k
            if k - curr.val in seen:
                return True
            seen.add(curr.val)

            # Visit children
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return False

    # # Binary Search:
    # def findTarget(self, root: TreeNode, k: int) -> bool:
    #     output = []
    #     self.inorder(root,output)
    #     l,r = 0 ,len(output) - 1
    #     while l < r:
    #         Sum = output[l] + output[r]
    #         if Sum == k:
    #             return True
    #         else:
    #             if Sum < k:
    #                 l += 1
    #             else:
    #                 r -= 1
    #     return False
    #
    # def inorder(self,root,output):
    #     if root == None:
    #         return
    #     else:
    #         self.inorder(root.left,output)
    #         output.append(root.val)
    #         self.inorder(root.right,output)

