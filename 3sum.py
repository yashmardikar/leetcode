###https://leetcode.com/problems/3sum/

###Brute Force

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        h1=dict()
        target=0
        op_list=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    w=nums[i]+nums[j]+nums[k]
                    if nums[i]+nums[j]+nums[k] == target:
                        l=sorted([ nums[i], nums[j], nums[k] ])
                        if l not in op_list:
                            op_list.append(l)
        return op_list
