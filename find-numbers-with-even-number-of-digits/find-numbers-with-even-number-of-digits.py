class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            #if len(str(num)) % 2 == 0:
            #    count+=1
            digCount = 0
            while num > 0: #num%10 != 0:
                num = num//10
                digCount += 1
            if digCount % 2 == 0:
                count += 1
        return count