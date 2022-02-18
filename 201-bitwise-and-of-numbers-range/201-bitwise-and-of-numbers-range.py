class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #only MSB matters, lower bits are cancelled by intermidiate 0's
        count = 0 #count how many bits needed to reach m==n
        while left != right:
            left = left >> 1
            right = right >> 1
            count +=1
        return right << count