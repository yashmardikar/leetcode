# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pFound = False
        self.qFound = False
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or (self.pFound and self.qFound):
            return None
        if root == p:
            self.pFound = True
            return p
        if root == q:
            self.qFound = True
            return q
        
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            #if both are not None, current node is root
            return root
        else:
            #Return whichever is not None
            #If both none, return None
            return left or right
            