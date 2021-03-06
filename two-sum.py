###Question: https://leetcode.com/problems/two-sum/
###Solution:
#O(n),O(n)

#Two Pass Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        h1=dict()
        #To find first pair we traverse in reverse array so that if a duplicate element exists
        #initial elements index remains in dictionary 
        for i in range(len(nums)-1,-1,-1):
            h1[nums[i]] = i


        for i in range(len(nums)):
            check_complement = h1.get(target - nums[i])
            if check_complement is not None:
                if check_complement == i :
                    pass
                else:
                    return [i,check_complement]
