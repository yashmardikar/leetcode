class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = {}
        #preprocessing arr in O(n)
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                visited[num] += 1
        
        #check for num visted only once
        for num, count in visited.items():
            if count == 1:
                return num
        