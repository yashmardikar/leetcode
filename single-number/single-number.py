class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        cache = set()
        for i in nums:
            if i in cache:
                cache.remove(i)
            else:
                cache.add(i)
        return cache.pop()
    
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor^nums[i]
        return xor
    
    def singleNumber2(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        xor = 0
        for i in nums:
            xor = xor^i
        return xor