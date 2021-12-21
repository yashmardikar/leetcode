#Brute Force

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count = 1
        num=1
        while count != n:
            num+=1
            if self.isUgly(num):
                count+=1
        return num
        
    ugly_cache=set([1,2,3,5])
    non_ugly_cache=set()
    def isUgly(self, n: int) -> bool:
        n_bak=n
        if n in self.ugly_cache:                    
            return True
        elif n in self.non_ugly_cache:
            return False
        
        for pnum in [2,3,5]:
            while n%pnum==0 and n>0:
                n//=pnum
                if n in self.ugly_cache:                    
                    self.ugly_cache.add(n_bak)
                    return True
                elif n in self.non_ugly_cache:
                    self.non_ugly_cache.add(n_bak)
                    return False
                
        if n==1:
            self.ugly_cache.add(n_bak)
        else:
            self.non_ugly_cache.add(n_bak)
        #print(self.ugly_cache)
        return n==1
