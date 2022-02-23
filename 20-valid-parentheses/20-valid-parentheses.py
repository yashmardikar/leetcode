class Solution:    
    
    def isValid(self, s: str) -> bool:
        l = []
        for char in s:
            if char == "(":
                l.append(char)
            elif char == ")":
                if l and l[-1] == "(":
                    l.pop()
                else:
                    return False
            if char == "[":
                l.append(char)
            elif char == "]":
                if l and l[-1] == "[":
                    l.pop()
                else:
                    return False
            if char == "{":
                l.append(char)
            elif char == "}":
                if l and l[-1] == "{":
                    l.pop()
                else:
                    return False
        return True if len(l)==0 else False