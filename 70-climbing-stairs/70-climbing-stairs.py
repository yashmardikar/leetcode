class Solution:
    def __init__(self):
        self.hmap = {1:1,2:2}
        
    def climbStairs(self, n: int) -> int:
        if n in self.hmap:
            return self.hmap[n]
        else:
            self.hmap[n-1] = self.climbStairs(n-1)
            self.hmap[n-2] = self.climbStairs(n-2)
        return self.hmap[n-1] + self.hmap[n-2]
        