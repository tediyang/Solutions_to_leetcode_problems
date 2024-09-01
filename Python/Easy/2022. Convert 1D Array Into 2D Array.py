from typing import List


class Solution:
  def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    if m*n != len(original):
      return []

    new_list = []
    i = 0
    while i < m:
      new_list.append(original[i * n: n * (i+1)])
      i += 1
    
    return new_list
