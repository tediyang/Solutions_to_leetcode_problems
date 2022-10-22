class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(str.split(s)[-1])