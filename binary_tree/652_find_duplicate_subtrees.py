# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        res = []
        path = defaultdict(int)
        def helper(node):
            if not node:
                return
            sub = tuple([helper(node.left), node.val, helper(node.right)])
            if sub in path and path[sub] == 1:
                res.append(node)
            path[sub] += 1
            return sub
        
        helper(root)
        return res
    
    def findDuplicateSubtrees_similar(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        visited = {}

        def helper(node, path=''):
            if not node:
                return '#'
            path += ','.join([str(node.val), helper(node.left, path), helper(node.right, path)])
            if path not in visited:
                visited[path] = 1
            else:
                visited[path] += 1
                if visited[path] == 2:
                    res.append(node)
            return path
        helper(root)
        return res