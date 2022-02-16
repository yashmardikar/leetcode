class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = nums.count(0)
        if zeroCount >= 2:
            return [0]*len(nums)
        
        product = 1
        zeroPresent = (zeroCount == 1) 
        flag = False
        
        for num in nums:
            if num == 0 and zeroCount == 1:
                continue
            product *= num
            
        new_arr = []
        for num in nums:
            if zeroPresent:
                if num == 0:
                    new_arr.append(product)
                else:
                    new_arr.append(0)
            else:
                new_arr.append(product//num)
        return new_arr