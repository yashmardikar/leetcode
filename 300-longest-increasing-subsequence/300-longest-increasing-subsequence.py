class Solution:    
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            #binary search
            low, hi = 0, len(arr)
            while low < hi:
                mid = (low+hi)//2
                if arr[mid] < num: 
                    low = mid+1
                else: 
                    hi = mid
            
            if low == len(arr):
                arr.append(num)
            else:
                arr[low] = num
                
        return len(arr)