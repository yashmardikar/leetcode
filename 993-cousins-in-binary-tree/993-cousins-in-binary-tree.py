# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x = x
        self.y = y
        #(parent_val, level)
        self.x_data = (None, None)
        self.y_data = (None, None)
        self.recur(root, level=1, parentVal = root.val)
        print(self.x_data, self.y_data)
        if self.x_data[0] != self.y_data[0] and self.x_data[1] == self.y_data[1]:
            return True
        return False
        
    def recur(self, root, level, parentVal):
        if self.x_data[0] is None or self.y_data[0] is None:
            #recur only if x,y are not found
            if root.val == self.x:
                self.x_data = (parentVal, level)
            if root.val == self.y:
                self.y_data = (parentVal, level)
            self.recur(root.left, level+1, root.val) if root.left else None
            self.recur(root.right, level+1, root.val) if root.right else None
            
            
