# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#from collections import defacultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.map = defaultdict(list)
        self.recur(root, 0, 0)
        #process map
        res = []
        #print(self.map)
        for col, val in sorted(self.map.items()):
            val.sort(key = lambda i: i[1])
            res.append([i for i,j in val])
        return res
    
    def recur(self, root, row, col):
        if root:
            self.recur(root.left, row+1, col-1) if root.left else None
            self.recur(root.right, row+1, col+1) if root.right else None
            self.map[col].append((root.val, row))
            
        
    
    