from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        distinct_count = 0
        for elem in arr:
            if counter[elem] > 1:
                continue
            distinct_count += 1
            if distinct_count == k:
                return elem
        
        return ""