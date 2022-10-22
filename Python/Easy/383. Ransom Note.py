class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans = []
        rans_len = len(ransomNote)

        mag = [i for i in magazine]

        for i in ransomNote:
            if i in mag:
                mag.remove(i)
                rans.append(i)

        if len(rans) == rans_len:
            return True

        else:
            return False