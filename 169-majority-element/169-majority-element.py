class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] == ceil(len(nums)/2):
                return num
            
            
        
        