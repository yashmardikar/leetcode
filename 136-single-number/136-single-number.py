class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            #a number xor with itself results zero
            #zero xor with anything is same number
            #eventually non repeating number is left
            xor ^= num
        return xor