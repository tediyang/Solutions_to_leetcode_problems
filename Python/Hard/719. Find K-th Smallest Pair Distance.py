from typing import List


class Solution:
  def smallestDistancePair(self, nums: List[int], k: int) -> int:
    #  create a list to store the count of the difference
    length = len(nums)
    max_value = max(nums) 
    
    # Steps
    # 1. Create a new list which stores all the difference using the max value
    # 2. Loop through all the items, get the difference of i and j and (index)increment the absolute
    # value by 1 depending on how many times they appear.
    # 3. Loop through the new array created.
    # 3a. Substract the value from k.
    # 3b. Then check if k is less than or equal to zero. if it is return the index of that value
    # 4. Finally return -1 indicating that the minimun diff couldn't be found.
 
    abs_diff = [0] * (max_value + 1)
    
    for i in range(length):
      for j in range(i + 1, length):
        abs_diff[abs(nums[i] - nums[j])] += 1
        
    
    for index, diff in enumerate(abs_diff):
      k -= diff
      
      if k <= 0:
        return index
      
    return -1
