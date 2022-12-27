# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        queue = deque([(0, root)])
        res = defaultdict(list)
        while queue:
            size = len(queue)
            for _ in range(size):
                ind, node = queue.popleft()
                res[ind].append(node.val)
                if node.left:
                    queue.append((ind-1, node.left))
                if node.right:
                    queue.append((ind+1, node.right))
        return [res[x] for x in sorted(res.keys())]