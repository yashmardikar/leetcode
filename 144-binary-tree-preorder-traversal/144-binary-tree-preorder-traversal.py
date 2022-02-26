# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        pass
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.lst = []
        self.preorderTraversalRecur(root)
        return self.lst
    
    def preorderTraversalRecur(self, root):
        if root:
            self.lst.append(root.val)
            if root.left:
                self.preorderTraversalRecur(root.left)
            if root.right:
                self.preorderTraversalRecur(root.right)