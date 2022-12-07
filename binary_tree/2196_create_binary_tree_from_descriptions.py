# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapping = defaultdict(TreeNode)
        child_set = set()
        
        for (parent, child, is_left) in descriptions:
            child_set.add(child)

            mapping[child].val = child
            mapping[parent].val = parent
                
            if is_left == 1:
                mapping[parent].left = mapping[child]
            else:
                mapping[parent].right = mapping[child]

        for node in mapping.keys():
            if node not in child_set:
                return mapping[node]
        return None