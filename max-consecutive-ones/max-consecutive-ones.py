class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCnt = 0
        for num in nums:
            if num == 1:
                count += 1
                maxCnt = max(maxCnt, count)
            if num !=1 :
                count = 0
        return maxCnt
                