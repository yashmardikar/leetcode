class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr)%k != 0:
            return False
        hmap = {}
        pairs = len(arr)//2
        
        for num in arr:
            comp = k - num%k #complement
            if comp in hmap and hmap[comp] != 0:
                hmap[k - num%k] -= 1
                pairs -= 1
            else:
                if num%k in hmap:
                    hmap[num%k] += 1
                else:
                    hmap[num%k] = 1
        zCount = hmap.get(0,0)
        if zCount%2 != 0:
            return False
        pairs -= zCount//2
        print(hmap)
        if pairs == 0:
            return True
        return False