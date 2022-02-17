from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        
        counter1 = Counter(s1)    
        counter2 = Counter(s2)
        #print(counter1 + counter2)
        uncommon_words = set(s1).symmetric_difference(set(s2))
        remove_set = set()
        for word in uncommon_words:
            if counter1.get(word, 0) > 1 or counter2.get(word, 0) > 1:
                remove_set.add(word)
        
        #print(counter1, counter2)
        #print(uncommon_words, remove_set)
        return uncommon_words - remove_set
        