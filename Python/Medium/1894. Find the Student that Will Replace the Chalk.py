from typing import List

class Solution:
  def chalkReplacer(self, chalk: List[int], k: int) -> int:
    summed = sum(chalk)

    if summed > k:
      return self.substract(chalk, k)

    k %= summed
    return self.substract(chalk, k)

  def substract(self, chalk: List[int], k: int) -> int:
    for i, num in enumerate(chalk):
      if num > k:
        return i
      k -= num
