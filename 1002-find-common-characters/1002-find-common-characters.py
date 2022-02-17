from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        rolling_counter = Counter(words[0])
        for i in range(1, len(words)):
            curr_counter = Counter(words[i])
            rolling_counter = curr_counter & rolling_counter
        
        #expand Counter
        result = [ ]
        for val, count in rolling_counter.items():
            result.extend([val]*count)
        
        return result
        
            