from typing import List

class Solution:
  def canSortArray(self, nums: List[int]) -> bool:
    sorted_nums = sorted(nums)
    if nums == sorted_nums:
      return True

    n = len(nums)
    for i in range(n):
      for j in range(0, n - i - 1):
        swap_1 = nums[j].bit_count()
        swap_2 = nums[j + 1].bit_count()
        if nums[j] > nums[j + 1] and swap_1 == swap_2:
          nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums == sorted_nums


# A better version (more efficient) of the above solution. [Not my code]
# class Solution:
#     def canSortArray(self, nums: List[int]) -> bool:
#         groups = []
#         curr = []
#         currBits = None
#         for num in nums:
#             if not currBits:
#                 currBits = num.bit_count()
#             if num.bit_count() == currBits:
#                 curr.append(num)
#             else:
#                 currBits = num.bit_count()
#                 groups.append(curr)
#                 curr = [num]
#         if curr:
#             groups.append(curr)

#         out = []
#         for g in groups:
#             out += sorted(g)
#         return out == sorted(nums)