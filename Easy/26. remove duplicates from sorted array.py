class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        num = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                num.append(nums[i])
                l += 1
        
        nums = num
      # return l, num
        return len(nums)