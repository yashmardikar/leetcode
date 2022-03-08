# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        if root:
            self.recur(root, val="")
        return sum( int(val,2) for val in self.arr )
        
    
    def recur(self, root, val):
        if root is None:
            #self.arr.append(val)
            return 
        val = val + str(root.val)
        
        if root.left is None and root.right is None:
            self.arr.append(val)
        
        self.recur(root.left, val)
        self.recur(root.right, val)
        
        