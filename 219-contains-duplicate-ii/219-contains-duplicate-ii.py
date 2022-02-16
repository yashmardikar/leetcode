class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        for i, num in enumerate(nums):
            if num not in hmap:
                hmap[num] = i
            elif abs(i-hmap[num]) <= k:
                    return True
            else:
                #replace value, append not needed. Discard initial reapeat index.
                hmap[num] = i
        return False