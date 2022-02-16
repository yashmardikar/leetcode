class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        map1 = {}
        #mapping word and their occurences
        for word in words1:
            if word not in map1:
                map1[word] = 1
            else:
                map1[word] += 1
        
        #keeping single occurence words
        new_words1 = []
        for word, count in map1.items():
            if count == 1:
                new_words1.append(word)
        
        map2 = {}
        #mapping word and their occurences
        for word in words2:
            if word not in map2:
                map2[word] = 1
            else:
                map2[word] += 1
        
        #keeping single occurence words
        new_words2 = []
        for word, count in map2.items():
            if count == 1:
                new_words2.append(word)
    
        return len(set(new_words2).intersection(set(new_words1)))