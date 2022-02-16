from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        result = 0
        for word in words1:
            if counter1[word] == 1 and counter2[word] == 1:
                result += 1
        return result
    