from typing import List

class Solution:
  def __init__(self):
    self.arrays = []

  def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    self.getSub(nums)

    data = sorted(self.arrays)
    return sum(data[left - 1: right]) % (10 ** 9 + 7)

  def getSub(self, num: List[int]) -> None:
    if len(num) == 0:
        return

    summed = 0
    i = 0
    while i < len(num):
      summed += num[i]
      self.arrays.append(summed)
      i += 1

    self.getSub(num[1:])

    return
