# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 or q2:
            level1 = []
            level2 = []
            if q1:
                q1len = len(q1)
                for _ in range(q1len):
                    node = q1.popleft()
                    if node:
                        level1.append(node.val)
                        q1.append(node.left)
                        q1.append(node.right)
                    else:
                        level1.append(None)
            if q2:
                q2len = len(q2)
                for _ in range(q2len):
                    node = q2.popleft()
                    if node:
                        level2.append(node.val)
                        q2.append(node.left)
                        q2.append(node.right)
                    else:
                        level2.append(None)
            if level1 != level2:
                return False
        return True