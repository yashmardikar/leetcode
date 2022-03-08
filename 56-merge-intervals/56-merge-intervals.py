class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for start, end in intervals:
            if not res:
                res.append([start, end])
            else:
                startp, endp = res[-1]    #previous start, previous end
                #update last range
                if startp <= start <= endp:
                    #check if new idx lies in prev range
                    res[-1][1] = max(end, endp)
                else:
                    #start new range
                    res.append([start,end])
        return res
                        
        