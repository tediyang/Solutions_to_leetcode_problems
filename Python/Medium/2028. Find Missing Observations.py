from typing import List

class Solution:
  def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    m, summed = len(rolls), sum(rolls)
    missing = ((m + n) * mean) - summed

    quotient, remainder = divmod(missing, n)
    if (remainder > 0 and (quotient + 1) > 6) or (quotient > 6 or quotient < 1):
      return []

    return [quotient + (1 if i < remainder else 0) for i in range(n)]
