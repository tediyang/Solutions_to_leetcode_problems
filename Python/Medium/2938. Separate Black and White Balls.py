class Solution:
  def minimumSteps(self, s: str) -> int:
    total, count = 0, 0
    for i in s[::-1]:
      if i == '1':
        total += count
      else:
        count += 1
    return total
