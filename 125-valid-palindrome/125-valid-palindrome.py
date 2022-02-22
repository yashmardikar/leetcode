class Solution:
    def isPalindrome(self, s: str) -> bool:
        alNumFilter = lambda x : "".join([char.lower() for char in x if char.isalnum() ])
        s = alNumFilter(s)
        return s == s[::-1]