class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        #process nums1 to get num occurance 
        for num in nums1:
            if num not in map1:
                map1[num]=1
            else:
                map1[num]+=1
        
        intersec = []
        # check of elem in nums2 already visted
        for num in nums2:
            if num in map1 and map1[num]!=0:
                intersec.append(num)
                map1[num]-=1
        
        return intersec
        