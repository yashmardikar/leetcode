class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #range function from last index to first to keep first found index in map
        maps = { target - nums[i] : i for i in range(len(nums))}
        print(maps)
        for i in range(len(nums)):
            if nums[i] in maps:
                #check if complement index and num index is different
                if maps[nums[i]] != i:
                    return maps[nums[i]],i
        return -1
            