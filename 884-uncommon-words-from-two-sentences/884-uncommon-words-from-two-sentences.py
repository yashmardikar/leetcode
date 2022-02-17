from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        master_list = s1.split(" ") + s2.split(" ")
        counter = Counter(master_list)
        res_set = set()
        for word, count in counter.items():
            if count == 1:
                res_set.add(word)
            
        return res_set