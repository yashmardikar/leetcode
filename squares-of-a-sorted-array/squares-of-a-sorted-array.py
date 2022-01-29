class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) < 1 :  
            return [i*i for i in nums]

        mid = 0
        while mid+1 <len(nums) and nums[mid+1] < abs(nums[mid]):
            mid += 1
        #-4 -1* 0 3 10
        #0* 1 1 2 3 4
        #-4 -3 -2 -1* 0
        #-1 -1* 0 0 1 1
        right = mid 
        left = mid - 1
        arr = []
        print(left,mid,right)
        while 1:
            numR = nums[right] if right < len(nums) else 10001
            numL = abs(nums[left]) if left >= 0 else 10001
            if numL > numR:
                arr.append(numR*numR)
                right += 1
            elif numL < numR:
                arr.append(numL*numL)
                left -= 1
            else:
                arr.append(numL*numL)
                arr.append(numL*numL)
                right += 1
                left -= 1
            #breaking condition
            #print(left, mid, right, numL, numR, nums, arr[:6], right >= len(nums) and left < 0 )
            if right >= len(nums) and left < 0:
                break
        return arr