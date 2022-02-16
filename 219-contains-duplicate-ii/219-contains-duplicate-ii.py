class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in hmap:
                hmap[num] = i
            elif abs(i-hmap[num]) <= k:
                    return True
            else:
                hmap[num] = i
        return False