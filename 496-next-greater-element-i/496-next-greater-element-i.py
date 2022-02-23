class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {num : idx for idx, num in enumerate(nums2) } 
        lst = []
        for num in nums1:
            idx = hmap[num]
            apnd = -1
            for i in range(idx+1,len(nums2)):
                if nums2[i] > num:
                    apnd = nums2[i]
                    break
            lst.append(apnd)
        return lst