# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        level = 0
        queue = [root]
        while queue:
            result.append([])
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if level%2 == 0:
                    result[level].append(node.val)
                else:
                    result[level].insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1
        return result
