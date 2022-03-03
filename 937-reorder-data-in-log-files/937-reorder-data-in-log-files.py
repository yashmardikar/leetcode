class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sorter(line):
            line = line.split(" ")
            identifier = line[0]
            isLetterLog = not line[1].isdigit()
            logPart = " ".join(line[1:])
            if isLetterLog:
                return (1, logPart, identifier)
            else:
                #its digit
                return (2, None, None)
            
            
        return sorted(logs, key = sorter)