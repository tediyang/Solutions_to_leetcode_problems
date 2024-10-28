from typing import List

class Solution:
  def longestSquareStreak(self, nums: List[int]) -> int:
    nums.sort()
    nums_set = set(nums)
    visited = set()
    max_streak = -1

    for num in nums:
      if num not in visited:
        current_streak = 1
        visited.add(num)
        current_num = num
        while current_num * current_num in nums_set:
          current_num *= current_num
          current_streak += 1

        max_streak = max(max_streak, current_streak) if current_streak > 1 else max_streak
                
    return max_streak
