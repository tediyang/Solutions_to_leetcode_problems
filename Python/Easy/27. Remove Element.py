class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = [n for n in nums if n != val]
        return len(num)