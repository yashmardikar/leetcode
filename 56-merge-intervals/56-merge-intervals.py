class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for start, end in intervals:
            if not res or start > res[-1][1]:
                #if first loop or curr start > last end(no overlap)
                res.append([start, end])
            else:
                #overlap, update end. (start is alredy >= prev start so no need to update) 
                res[-1][1] = max(end, res[-1][1])
        return res        
        