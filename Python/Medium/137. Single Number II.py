class Solution:
    """
      Solution module to Problem 137
    """
    def singleNumber(self, nums: list[int]) -> int:
        """ Return non-duplicate number """
        for i in nums:
            if nums.count(i) == 1:
                return i
