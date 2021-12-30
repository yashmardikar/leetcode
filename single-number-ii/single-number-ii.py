class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        #add to s1 when only 1 occurence is found yet
        s1 = set()
        #add to s2 when 2 occurences found yet
        s2 = set()
        
        for n in nums:
            #means num was found once before
            c1 = n in s1 
            #means num was found twice before
            c2 = n in s2
            
            #num was never found before
            if (n not in s1) and (n not in s2):
                #number is occuring for first time
                s1.add(n)
            elif not c2:
                #number is occuring for second time
                s2.add(n)
                s1.remove(n)
            elif c2:
                s2.remove(n)
        
        return s1.pop()
    
    def singleNumber(self, nums: List[int]) -> int:
        unique_num_sum = sum(set(nums))
        
        # repeating numbers are added 3 times except unique num
        all_nums_sum = sum(nums)
        
        # 3x-x => 2x. only unique num remains
        unique_num = 3 * unique_num_sum - all_nums_sum
        
        #returning int, not float
        return int(unique_num/2)