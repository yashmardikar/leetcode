class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache=set()
        for i in nums:
            if i in cache:
                cache.remove(i)
            else:
                cache.add(i)
        return cache.pop()