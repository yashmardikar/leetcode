class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        #time complexity: O(n)
        #space complexity: O(n/3)
        
        # add when num count is exactly 1
        s1 = set()
        # add when num count is exactly 2
        s2 = set()
        
        for n in nums:
            #num was never found before
            if (n not in s1) and (n not in s2):
                #number is occuring for first time
                s1.add(n)
            elif not c2:
                #number is occuring for second time
                s2.add(n)
                s1.remove(n)
            elif c2:
                # number occured 3rd time
                s2.remove(n)
        
        return s1.pop()
    
    def singleNumber(self, nums: List[int]) -> int:
        #time complexity: O(2n)
        #space complexity: O(n/3)
        
        unique_num_sum = sum(set(nums))
        
        # repeating numbers are added 3 times except unique num
        all_nums_sum = sum(nums)
        
        # 3x-x => 2x. only unique num remains
        unique_num = 3 * unique_num_sum - all_nums_sum
        
        #returning int, not float
        return int(unique_num/2)
    
    