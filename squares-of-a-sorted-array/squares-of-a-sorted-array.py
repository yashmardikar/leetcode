class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #nlogn
        new_nums=[]
        for i in range(len(nums)):
            new_nums.append(nums[i]*nums[i])
        new_nums.sort()
        return new_nums